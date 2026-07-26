from machine import Pin, I2C
import ssd1306
from time import sleep
import time
from screens import *
from displayFunctions import *
import usb.device
from usb.device.keyboard import KeyboardInterface
from usb.device.mouse import MouseInterface
import _thread
from consumer import ConsumerInterface
import json
import sys
import os

with open("config.json", "r") as file:
    data = json.load(file)

    activated = data["Activated"]

    serialNumber = data["Serial Number"]

    softwareVersion = data["Software Version"]
    
    sleepTime = data["Sleep Time"]

hardwareVersionMajor, hardwareVersionMinor, hardwareVersionMicro = map(int, "v1.0.0".lstrip("v").split("."))
hardwareVersionBcd = (hardwareVersionMajor << 8) | (hardwareVersionMinor << 4) | hardwareVersionMicro

keyboard = KeyboardInterface()
mouse = MouseInterface()
consumer = ConsumerInterface()

i2c = I2C(sda=Pin("OLED_SDA"), scl=Pin("OLED_SCL"))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

macroButtonPins = ["ENCODER_BTN",
                   "BTN_1", "BTN_2", "BTN_3", "BTN_4",
                   "BTN_5", "BTN_6", "BTN_7", "BTN_8",
                   "BTN_9", "BTN_10", "BTN_11", "BTN_12"]

macroButtons = []

for pin in macroButtonPins:
    macroButtons.append(Pin(pin, Pin.IN, Pin.PULL_UP))

display.contrast(0)

if activated:
    usb.device.get().init(keyboard,
                          consumer,
                          mouse,
                          builtin_driver=True,
                          manufacturer_str="Jacob Waters",
                          product_str="Macro Pad",
                          serial_str=serialNumber,
                          id_vendor=4617,
                          id_product=31291,
                          bcd_device=hardwareVersionBcd)

startUpScreen(display, softwareVersion)
increaseBrightness(display, speed=0.02)

if not activated:
    notActivatedScreen(display)
    
    while True:
        pass

layers = len(os.listdir("/Layers"))

if layers == 0:
    noLayersScreen(display)
    
    while True:
        pass

loadedLayers = {}

for layer in range(1, layers + 1):
    sys.path.append(f"/Layers/{layer}/")
    layerMod = __import__(f"Layer{layer}")
    keysMod = __import__(f"Keys{layer}")
    
    loadedLayers[layer] = {
        "layer": layerMod,
        "keys": keysMod,
    }

currentLayer = 1

display.fill(0)

loadedLayers[currentLayer]["layer"].layer(display)

last_press = time.ticks_ms()
lock = _thread.allocate_lock()
displayBrightnessLowered = False
displaySleep = False

R_START     = 0x0
R_CW_FINAL  = 0x1
R_CW_BEGIN  = 0x2
R_CW_NEXT   = 0x3
R_CCW_BEGIN = 0x4
R_CCW_FINAL = 0x5
R_CCW_NEXT  = 0x6

DIR_CW  = 0x10
DIR_CCW = 0x20

ttable = (
    (R_START,    R_CW_BEGIN,  R_CCW_BEGIN, R_START),
    (R_CW_NEXT,  R_START,     R_CW_FINAL,  R_START | DIR_CW),
    (R_CW_NEXT,  R_CW_BEGIN,  R_START,     R_START),
    (R_CW_NEXT,  R_CW_BEGIN,  R_CW_FINAL,  R_START),
    (R_CCW_NEXT, R_START,     R_CCW_BEGIN, R_START),
    (R_CCW_NEXT, R_CCW_FINAL, R_START,     R_START | DIR_CCW),
    (R_CCW_NEXT, R_CCW_FINAL, R_CCW_BEGIN, R_START),
)

encoderA = Pin("ENCODER_A", Pin.IN, Pin.PULL_UP)
encoderB = Pin("ENCODER_B", Pin.IN, Pin.PULL_UP)

encoder_state   = R_START
encoder_delta   = 0
encoder_velocity = 0.0
last_encoder_ms = time.ticks_ms()

def encoder_handler(pin):
    global encoder_state, encoder_delta, last_press

    pinstate = (encoderA.value() << 1) | encoderB.value()
    encoder_state = ttable[encoder_state & 0x0F][pinstate]
    direction = encoder_state & 0x30

    if direction == DIR_CW:
        encoder_delta += 1
        
    elif direction == DIR_CCW:
        encoder_delta -= 1

    if direction:
        with lock:
            last_press = time.ticks_ms()

encoderA.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=encoder_handler)
encoderB.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=encoder_handler)

stopIdleWatcher = False

def idleWatcher():
    global last_press, displayBrightnessLowered, displaySleep

    while not stopIdleWatcher:
        with lock:
            elapsed = time.ticks_diff(time.ticks_ms(), last_press)

        if elapsed >= sleepTime:
            if not displayBrightnessLowered:
                decreaseBrightness(display)
                displayBrightnessLowered = True

            elif not displaySleep:
                display.poweroff()
                displaySleep = True

            with lock:
                last_press = time.ticks_ms()
                
        time.sleep_ms(500)
        
def encoderLongPress():
    global currentLayer
    
    if layers > 1:        
        if currentLayer != layers:
            currentLayer += 1
            display.fill(0)
            loadedLayers[currentLayer]["layer"].layer(display)
            
        else:
            currentLayer = 1
            display.fill(0)
            loadedLayers[currentLayer]["layer"].layer(display)
            
_thread.start_new_thread(idleWatcher, ())

prev = [not btn.value() for btn in macroButtons]

pressStartTimes = [None] * len(macroButtons)
nextRepeatTime  = [None] * len(macroButtons)

encoderPressStart = None
encoderLongPressFired = False
encoder_last_dir = 0
encoder_dir_lock_until = 0

while True:
    now = time.ticks_ms()
    dt = time.ticks_diff(now, last_encoder_ms) / 1000.0
    last_encoder_ms = now

    encoder_velocity *= max(0.0, 1.0 - (dt * 7.5))

    if encoder_delta != 0:
        raw = encoder_delta
        encoder_delta = 0

        current_dir = 1 if raw > 0 else -1
        if current_dir != encoder_last_dir and time.ticks_diff(now, encoder_dir_lock_until) < 0:
            raw = 0
            
        else:
            encoder_last_dir = current_dir
            
            if abs(encoder_velocity) > 3.0:
                encoder_dir_lock_until = time.ticks_add(now, 40)

        if raw != 0:
            encoder_velocity += raw * 1.2

            if encoder_velocity > 10:
                encoder_velocity = 10.0
            elif encoder_velocity < -10:
                encoder_velocity = -10.0

    steps = int(round(encoder_velocity))

    if abs(steps) >= 2 and abs(encoder_velocity) < 1.7:
        steps = 1 if encoder_velocity > 0 else -1

    if steps != 0:
        encoder_velocity *= 0.55

        if displaySleep:
            displaySleep = False
            displayBrightnessLowered = False
            display.poweron()
            increaseBrightness(display)
            
        elif displayBrightnessLowered:
            displayBrightnessLowered = False
            increaseBrightness(display)
            
        loadedLayers[currentLayer]["keys"].rotaryChecker(keyboard, consumer, mouse, steps)

    for i, btn in enumerate(macroButtons):
        pressed = not btn.value()
        
        if i == 0:
            if pressed and not prev[i]:
                encoderPressStart = time.ticks_ms()
                encoderLongPressFired = False

                if displaySleep:
                    displaySleep = False
                    displayBrightnessLowered = False
                    display.poweron()
                    increaseBrightness(display)
                    
                elif displayBrightnessLowered:
                    displayBrightnessLowered = False
                    increaseBrightness(display)

                with lock:
                    last_press = time.ticks_ms()

            elif pressed and prev[i] and not encoderLongPressFired:
                if encoderPressStart is not None and time.ticks_diff(time.ticks_ms(), encoderPressStart) >= 1000:
                    encoderLongPressFired = True
                    encoderLongPress()

            elif not pressed and prev[i]:
                if not encoderLongPressFired:
                    loadedLayers[currentLayer]["keys"].keyChecker(keyboard, consumer, mouse, 0)

            prev[i] = pressed
            
        else:
            if pressed != prev[i]:
                if pressed:
                    loadedLayers[currentLayer]["keys"].keyChecker(keyboard, consumer, mouse, i)

                    pressStartTimes[i] = time.ticks_ms()
                    nextRepeatTime[i] = time.ticks_add(pressStartTimes[i], 500)

                    if displaySleep:
                        displaySleep = False
                        displayBrightnessLowered = False
                        display.poweron()
                        increaseBrightness(display)

                    elif displayBrightnessLowered:
                        displayBrightnessLowered = False
                        increaseBrightness(display)

                    with lock:
                        last_press = time.ticks_ms()

                else:
                    pressStartTimes[i] = None
                    nextRepeatTime[i] = None

                prev[i] = pressed

            elif pressed and nextRepeatTime[i] is not None:
                now = time.ticks_ms()
                if time.ticks_diff(now, nextRepeatTime[i]) >= 0:
                    loadedLayers[currentLayer]["keys"].keyChecker(keyboard, consumer, mouse, i)
                    nextRepeatTime[i] = time.ticks_add(now, 30)

                    with lock:
                        last_press = now
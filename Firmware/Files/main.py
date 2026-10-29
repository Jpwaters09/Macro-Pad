from machine import Pin, I2C, Timer
import machine
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

if activated or serialNumber:
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

if not activated or not serialNumber:
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

encoderA = Pin("ENCODER_A", Pin.IN, Pin.PULL_UP)
encoderB = Pin("ENCODER_B", Pin.IN, Pin.PULL_UP)

ENCODER_REVERSED = False
ENCODER_REVERSE_LOCK_MS = 120
ENCODER_ACCEL = True
ACCEL_FAST_MS = 45
ACCEL_MED_MS = 90
ENCODER_MAX_SEND = 8

_QEM = (0, -1,  1, 0,
        1,  0,  0, -1,
       -1,  0,  0, 1,
        0,  1, -1, 0)

ENCODER_DEBOUNCE = 4

_a0 = encoderA.value()
_b0 = encoderB.value()
encoder_state = [_a0, _b0, 0, 0, (_a0 << 1) | _b0, 0, 0]

def encoder_sample(timer, A=encoderA, B=encoderB, S=encoder_state, Q=_QEM, DEB=ENCODER_DEBOUNCE):
    a = A.value()

    if a != S[0]:
        S[2] += 1

        if S[2] >= DEB:
            S[0] = a
            S[2] = 0

    else:
        S[2] = 0

    b = B.value()

    if b != S[1]:
        S[3] += 1

        if S[3] >= DEB:
            S[1] = b
            S[3] = 0

    else:
        S[3] = 0

    new = (S[0] << 1) | S[1]
    prev = S[4]

    if new != prev:
        if (new ^ prev) == 3:
            S[6] += 1

            if S[6] >= 40:
                S[4] = new
                S[6] = 0

        else:
            S[5] += Q[(prev << 2) | new]
            S[4] = new
            S[6] = 0

    else:
        S[6] = 0

encoder_timer = Timer()

encoder_timer.init(
    mode=Timer.PERIODIC,
    freq=8000,
    callback=encoder_sample,
    hard=True
)

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

lastStepDir = 0
lastStepTime = time.ticks_ms()

dbgSent = 0
dbgLocked = 0
dbgWorstUs = 0
dbgLastPrint = time.ticks_ms()

encoderPressStart = None
encoderLongPressFired = False

while True:
    irq_state = machine.disable_irq()

    raw = encoder_state[5]

    if raw >= 4:
        steps = raw // 4

    elif raw <= -4:
        steps = -((-raw) // 4)

    else:
        steps = 0
    encoder_state[5] -= steps * 4

    machine.enable_irq(irq_state)

    if ENCODER_REVERSED:
        steps = -steps

    accel = 1

    if steps != 0:
        now = time.ticks_ms()
        stepGap = time.ticks_diff(now, lastStepTime)
        stepDir = 1 if steps > 0 else -1
        if stepDir != lastStepDir and stepGap < ENCODER_REVERSE_LOCK_MS:
            dbgLocked += abs(steps)
            steps = 0

        else:
            if ENCODER_ACCEL and stepDir == lastStepDir:
                if stepGap < ACCEL_FAST_MS:
                    accel = 3

                elif stepGap < ACCEL_MED_MS:
                    accel = 2

            lastStepDir = stepDir
            lastStepTime = now

    if steps != 0:
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

        direction = 1 if steps > 0 else -1
        sendCount = min(abs(steps) * accel, ENCODER_MAX_SEND)
        sendStart = time.ticks_us()

        if steps > 0:
            for _ in range(sendCount):
                loadedLayers[currentLayer]["keys"].rotaryChecker(
                    keyboard,
                    consumer,
                    mouse,
                    1
                )

        else:
            for _ in range(sendCount):
                loadedLayers[currentLayer]["keys"].rotaryChecker(
                    keyboard,
                    consumer,
                    mouse,
                    -1
                )

        dbgSent += sendCount
        sendUs = time.ticks_diff(time.ticks_us(), sendStart)
        if sendUs > dbgWorstUs:
            dbgWorstUs = sendUs

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
                if encoderPressStart is not None and time.ticks_diff(time.ticks_ms(), encoderPressStart) >= 500:
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
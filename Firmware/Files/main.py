from machine import Pin, I2C
import ssd1306
from time import sleep
import time
from screens import *
from displayFunctions import *
import usb.device
from usb.device.keyboard import KeyboardInterface
import _thread
from keys import *
from consumer import ConsumerInterface
import json

with open("config.json", "r") as file:
    data = json.load(file)
    
    usbHidMode = data["USB HID Mode"]
    
    productManufacturer = data["Product Manufacturer"]
    productName = data["Product Name"]
    serialNumber = data["Serial Number"]
    vendorID = data["Vendor ID"]
    productID = data["Product ID"]
    
    version = data["Version"]

keyboard = KeyboardInterface()
consumer = ConsumerInterface()

if usbHidMode:
    usb.device.get().init(keyboard,
                           consumer,
                           builtin_driver=True,
                           manufacturer_str=productManufacturer,
                           product_str=productName,
                           serial_str=serialNumber,
                           id_vendor=vendorID,
                           id_product=productID)

i2c = I2C(sda=Pin(0), scl=Pin(1))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.contrast(100)
startUpScreen(display, version)
increaseBrightness(display, speed=0.05)

encoderA = Pin(3, Pin.IN, Pin.PULL_UP)
encoderB = Pin(4, Pin.IN, Pin.PULL_UP)

macroButtonPins = [2,
                   5, 6, 7, 8,
                   9, 10, 11, 12,
                   13, 14, 15, 16]

macroButtons = []

for pin in macroButtonPins:
    macroButtons.append(Pin(pin, Pin.IN, Pin.PULL_UP))

homeScreen(display)

last_press = time.ticks_ms()
lock = _thread.allocate_lock()
displayBrightnessLowered = False
displaySleep = False

encoder_delta = 0
encoder_moved = False
last_encoder_time = 0

def encoder_handler(pin):
    global encoder_delta, encoder_moved, last_encoder_time, last_press
    
    now = time.ticks_ms
    
    if time.ticks_diff(now, last_encoder_time) < 5:
        return
    
    last_encoder_time = now
    
    if encoderB.value() != encoderA.value():
        encoder_delta = 1
        
    else:
        encoder_delta = -1
        
    encoder_moved = True
    
    with lock:
        last_press = time.ticks_ms()
        
encoderA.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=encoder_handler)

def idleWatcher():
    global last_press, displayBrightnessLowered, displaySleep
    
    while True:
        with lock:
            elapsed = time.ticks_diff(time.ticks_ms(), last_press)
            
        if elapsed >= 60000:
            if not displayBrightnessLowered:
                decreaseBrightness(display)
                displayBrightnessLowered = True
                
            elif not displaySleep:
                display.poweroff()
                displaySleep = True
                
            with lock:
                last_press = time.ticks_ms()
        time.sleep_ms(500)

_thread.start_new_thread(idleWatcher, ())

prev = [True] * len(macroButtons)

while True:
    if encoder_moved:
        encoder_moved = False
        
        if displaySleep:
            displaySleep = False
            displayBrightnessLowered = False
            display.poweron()
            increaseBrightness(display)
        
        elif displayBrightnessLowered:
            displayBrightnessLowered = False
            increaseBrightness(display)
            
        rotaryChecker(keyboard, consumer, encoder_delta)
        
    for i, btn in enumerate(macroButtons):
        pressed = not btn.value()
        
        if pressed != prev[i]:
            if pressed:
                keyChecker(keyboard, consumer, i)
                
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
                        
            prev[i] = pressed
        
    time.sleep_ms(10)
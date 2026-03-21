from usb.device.keyboard import KeyCode
from consumer import ConsumerCode
from time import sleep

def rotaryChecker(keyboard, consumer, delta):
    if delta == 1:
        consumer.send_code(ConsumerCode.VOLUME_UP)
        
    if delta == -1:
        consumer.send_code(ConsumerCode.VOLUME_DOWN)

def keyChecker(keyboard, consumer, key):
    if key == 0:
        consumer.send_code(ConsumerCode.MUTE)
        
    if key == 1:
        keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.Z])
        
    if key == 2:
        keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.Y])
        
    if key == 3:
        keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.C])
        
    if key == 4:
        keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.V])
        
    if key == 5:
        keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.X])
        
    if key == 6:
        keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.A])
        
    if key == 7:
        keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.F])
        
    if key == 8:
        keyboard.send_keys([KeyCode.PRINTSCREEN])
        
    if key == 9:
        keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.N])
        
    if key == 10:
        keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.S])
        
    if key == 11:
        keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.O])
        
    if key == 12:
        keyboard.send_keys([KeyCode.LEFT_UI, KeyCode.L])
        
    keyboard.send_keys([])
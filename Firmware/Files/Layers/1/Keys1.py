from time import sleep
from keycodes import *

def rotaryChecker(keyboard, consumer, mouse, delta):
    # none
    
    if delta == 1:
        none(keyboard, consumer, mouse)
        
    if delta == -1:
        none(keyboard, consumer, mouse)
        
    keyboard.send_keys([])

def keyChecker(keyboard, consumer, mouse, key):
    if key == 0:
        none(keyboard, consumer, mouse)
        
    if key == 1:
        none(keyboard, consumer, mouse)
        
    if key == 2:
        none(keyboard, consumer, mouse)
        
    if key == 3:
        none(keyboard, consumer, mouse)
        
    if key == 4:
        none(keyboard, consumer, mouse)
        
    if key == 5:
        none(keyboard, consumer, mouse)
        
    if key == 6:
        none(keyboard, consumer, mouse)
        
    if key == 7:
        none(keyboard, consumer, mouse)
        
    if key == 8:
        none(keyboard, consumer, mouse)
        
    if key == 9:
        none(keyboard, consumer, mouse)
        
    if key == 10:
        none(keyboard, consumer, mouse)
        
    if key == 11:
        none(keyboard, consumer, mouse)
        
    if key == 12:
        none(keyboard, consumer, mouse)
        
    keyboard.send_keys([])
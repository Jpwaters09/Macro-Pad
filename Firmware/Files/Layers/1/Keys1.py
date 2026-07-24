from time import sleep
from keycodes import *

def rotaryChecker(keyboard, consumer, mouse, delta):
    # volume
    
    if delta == 1:
        volumeUp(keyboard, consumer, mouse)
        
    if delta == -1:
        volumeDown(keyboard, consumer, mouse)
        
    keyboard.send_keys([])

def keyChecker(keyboard, consumer, mouse, key):
    if key == 0:
        mute(keyboard, consumer, mouse)
        
    if key == 1:
        copy(keyboard, consumer, mouse)
        
    if key == 2:
        paste(keyboard, consumer, mouse)
        
    if key == 3:
        cut(keyboard, consumer, mouse)
        
    if key == 4:
        selectAll(keyboard, consumer, mouse)
        
    if key == 5:
        undo(keyboard, consumer, mouse)
        
    if key == 6:
        redo(keyboard, consumer, mouse)
        
    if key == 7:
        find(keyboard, consumer, mouse)
        
    if key == 8:
        printscreen(keyboard, consumer, mouse)
        
    if key == 9:
        newFile(keyboard, consumer, mouse)
        
    if key == 10:
        openFile(keyboard, consumer, mouse)
        
    if key == 11:
        save(keyboard, consumer, mouse)
        
    if key == 12:
        lock(keyboard, consumer, mouse)
        
    keyboard.send_keys([])
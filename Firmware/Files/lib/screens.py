import framebuf
from displayFunctions import *

    
def programmerScreen(display):
    display.fill(0)
    
    display.text("Device Connected", 0, 22, 1)
    display.text("To Programmer", 12, 33, 1)

    display.show()
    
def noLayersScreen(display):
    display.fill(0)
    
    display.text("No Layers Loaded", 0, 3, 1)
    display.text("Add Layers Using", 0, 18, 1)
    display.text("The Programmer", 8, 29, 1)
    display.text("macropad.", 28, 43, 1)
    display.text("jpwaters09.com", 8, 54, 1)
    
    display.show()

def startUpScreen(display, version):
    display.fill(0)
    
    display.text("Macro Pad", 28, 15, 1)
    centreX(display, version, 47, 1)
    
    display.show()

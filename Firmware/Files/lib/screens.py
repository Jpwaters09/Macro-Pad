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

def updateScreen(display):
<<<<<<< HEAD
    display.fill(0)
    
=======
>>>>>>> bf6fbf85ad81311516e7025d72a618af91539d2c
    display.text("Macro Pad", 28, 11, 1)
    display.text("Updating...", 20, 47, 1)
    
    display.show()
<<<<<<< HEAD

def notActivatedScreen(display):
    display.fill(0)
    
    display.text("Not Activated", 12, 3, 1)
    display.text("Activate At:", 16, 18, 1)
    display.text("macropad.", 28, 29, 1)
    display.text("jpwaters09.com/", 4, 40, 1)
    display.text("Activate", 32, 51, 1)
    
    display.show()
=======
>>>>>>> bf6fbf85ad81311516e7025d72a618af91539d2c

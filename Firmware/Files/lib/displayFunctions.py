from time import sleep

def decreaseBrightness(display, speed=0.01):
    for brightness in reversed(range(1, 101)):
        display.contrast(brightness)
        sleep(speed)
        
def increaseBrightness(display, speed=0.01):
    for brightness in range(1, 101):
        display.contrast(brightness)
        sleep(speed)
        
def centreX(display, text, y, colour):
    textLength = len(text)
    textPixelLength = textLength * 8
    
    x = 64 - (textPixelLength // 2)
    
    display.text(text, x, y, colour)
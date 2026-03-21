from time import sleep

def decreaseBrightness(display, speed=0.01):
    for brightness in reversed(range(1, 101)):
        display.contrast(brightness)
        sleep(speed)
        
def increaseBrightness(display, speed=0.01):
    for brightness in range(1, 101):
        display.contrast(brightness)
        sleep(speed)
import framebuf
from icons import *

def centreX(display, text, y, colour):
    textLength = len(text)
    textPixelLength = textLength * 8
    
    x = 64 - (textPixelLength // 2)
    
    display.text(text, x, y, colour)

def startUpScreen(display, version):
    display.fill(0)
    
    display.text("Macro Pad", 28, 15, 1)
    centreX(display, version, 28, 1)
    display.text("By Jacob Waters", 4, 49, 1)
    
    display.show()

    
def homeScreen(display):
    display.fill(0)
    
    volumeLoudIconFb = framebuf.FrameBuffer(volumeLoudIcon, 20, 16, framebuf.MONO_HLSB)
    display.blit(volumeLoudIconFb, 104, 2)

    volumeMuteIconFb = framebuf.FrameBuffer(volumeMuteIcon, 18, 16, framebuf.MONO_HLSB)
    display.blit(volumeMuteIconFb, 105, 23)

    settingsIconFb = framebuf.FrameBuffer(settingsIcon, 14, 16, framebuf.MONO_HLSB)
    display.blit(settingsIconFb, 107, 46)

    undoIconFb = framebuf.FrameBuffer(undoIcon, 20, 20, framebuf.MONO_HLSB)
    display.blit(undoIconFb, 2, 0)

    redoIconFb = framebuf.FrameBuffer(redoIcon, 20, 20, framebuf.MONO_HLSB)
    display.blit(redoIconFb, 27, 0)

    copyIconFb = framebuf.FrameBuffer(copyIcon, 20, 20, framebuf.MONO_HLSB)
    display.blit(copyIconFb, 52, 0)

    pasteIconFb = framebuf.FrameBuffer(pasteIcon, 20, 20, framebuf.MONO_HLSB)
    display.blit(pasteIconFb, 77, 1)

    cutIconFb = framebuf.FrameBuffer(cutIcon, 20, 20, framebuf.MONO_HLSB)
    display.blit(cutIconFb, 2, 22)

    selectAllIconFb = framebuf.FrameBuffer(selectAllIcon, 20, 20, framebuf.MONO_HLSB)
    display.blit(selectAllIconFb, 27, 22)

    screenshotIconFb = framebuf.FrameBuffer(screenshotIcon, 20, 20, framebuf.MONO_HLSB)
    display.blit(screenshotIconFb, 77, 22)

    findIconFb = framebuf.FrameBuffer(findIcon, 20, 20, framebuf.MONO_HLSB)
    display.blit(findIconFb, 52, 22)

    lockIconFb = framebuf.FrameBuffer(lockIcon, 20, 20, framebuf.MONO_HLSB)
    display.blit(lockIconFb, 77, 43)

    saveIconFb = framebuf.FrameBuffer(saveIcon, 20, 20, framebuf.MONO_HLSB)
    display.blit(saveIconFb, 27, 44)

    openFileIconFb = framebuf.FrameBuffer(openFileIcon, 20, 20, framebuf.MONO_HLSB)
    display.blit(openFileIconFb, 52, 44)
    
    newFileIconFb = framebuf.FrameBuffer(newFileIcon, 20, 20, framebuf.MONO_HLSB)
    display.blit(newFileIconFb, 2, 44)
    
    display.rect(0, 0, 24, 20, 1)
    display.rect(0, 22, 24, 20, 1)
    display.rect(0, 44, 24, 20, 1)
    display.rect(25, 0, 24, 20, 1)
    display.rect(50, 0, 24, 20, 1)
    display.rect(75, 0, 24, 20, 1)
    display.rect(25, 22, 24, 20, 1)
    display.rect(50, 22, 24, 20, 1)
    display.rect(75, 22, 24, 20, 1)
    display.rect(25, 44, 24, 20, 1)
    display.rect(50, 44, 24, 20, 1)
    display.rect(75, 44, 24, 20, 1)
    display.rect(100, 0, 28, 42, 1)
    display.line(101, 21, 126, 21, 1)
    display.rect(100, 44, 28, 20, 1)
    display.line(101, 20, 126, 20, 1)

    display.show()

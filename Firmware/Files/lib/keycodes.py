from usb.device.keyboard import KeyCode
from consumer import ConsumerCode

def none(keyboard, consumer, mouse):
    pass

def copy(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.C])
    
def paste(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.V])
    
def cut(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.X])
    
def undo(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.Z])
    
def redo(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.Y])
    
def selectAll(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.A])
    
def find(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.F])

def bold(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.B])

def underline(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.U])

def italic(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.I])

def jumpWordLeft(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.LEFT])

def jumpWordRight(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.RIGHT])

def deleteWordLeft(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.BACKSPACE])
    
def deleteWordLeft(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.DELETE])
      
def newFile(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.N])
    
def save(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.S])
    
def saveAs(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.LEFT_SHIFT, KeyCode.S])

def openFile(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.O])
    
def printFile(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.P])
    
def closeTab(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.W])
   
def nextTab(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.TAB])
   
def prevTab(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.LEFT_SHIFT, KeyCode.TAB])
   
def newTab(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.T])
   
def openClosedTab(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.LEFT_SHIFT, KeyCode.T])
   
def zoomIn(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.LEFT_SHIFT, KeyCode.EQUAL])
  
def zoomOut(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.MINUS])
    
def lock(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_UI, KeyCode.L])
    
def printscreen(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.PRINTSCREEN])
    
def volumeUp(keyboard, consumer, mouse):
    consumer.send_code(ConsumerCode.VOLUME_UP)
    
def volumeDown(keyboard, consumer, mouse):
    consumer.send_code(ConsumerCode.VOLUME_DOWN)
    
def mute(keyboard, consumer, mouse):
    consumer.send_code(ConsumerCode.MUTE)
    
def backTab(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_ALT, KeyCode.LEFT])
    
def forwardTab(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_ALT, KeyCode.RIGHT])
    
def reloadTab(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.R])

def bookmarkPage(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.D])

def openHistory(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.H])

def openDownloads(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.J])
    
def resetZoom(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.N0])
    
def incognitoWindow(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.LEFT_SHIFT, KeyCode.N])
      
def fullScreen(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.F11])
    
def focusToSearch(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL, KeyCode.L])
    
def scrollUp(keyboard, consumer, mouse):
    mouse.scroll(1)
    
def scrollDown(keyboard, consumer, mouse):
    mouse.scroll(-1)

def scrollLeft(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT])
    mouse.scroll(1)
    
def scrollRight(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT])
    mouse.scroll(-1)

def changeNextWindow(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_ALT, KeyCode.TAB])
    
def changePrevWindow(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_ALT, KeyCode.LEFT_SHIFT, KeyCode.TAB])
    
def middleClick(keyboard, consumer, mouse):
    mouse.click_middle(True)
    mouse.click_middle(False)
    
def leftClick(keyboard, consumer, mouse):
    mouse.click_left(True)
    mouse.click_left(False)
    
def rightClick(keyboard, consumer, mouse):
    mouse.click_right(True)
    mouse.click_right(False)
    
def lowerCaseA(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.A])
    
def upperCaseA(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.A])
    
def lowerCaseB(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.B])
    
def upperCaseB(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.B])
        
def lowerCaseC(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.C])
    
def upperCaseC(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.C])
    
def lowerCaseD(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.D])
    
def upperCaseD(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.D])
        
def lowerCaseE(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.E])
    
def upperCaseE(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.E])
        
def lowerCaseF(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.F])
    
def upperCaseF(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.F])
        
def lowerCaseG(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.G])
    
def upperCaseG(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.G])
        
def lowerCaseH(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.H])
    
def upperCaseH(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.H])
        
def lowerCaseI(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.I])
    
def upperCaseI(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.I])
        
def lowerCaseJ(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.J])
    
def upperCaseJ(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.J])
        
def lowerCaseK(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.K])
    
def upperCaseK(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.K])
        
def lowerCaseL(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.L])
    
def upperCaseL(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.L])
        
def lowerCaseM(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.M])
    
def upperCaseM(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.M])
        
def lowerCaseN(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.N])
    
def upperCaseN(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.N])
        
def lowerCaseO(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.O])
    
def upperCaseO(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.O])
        
def lowerCaseP(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.P])
    
def upperCaseP(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.P])
        
def lowerCaseQ(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.Q])
    
def upperCaseQ(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.Q])
        
def lowerCaseR(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.R])
    
def upperCaseR(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.R])
        
def lowerCaseS(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.S])
    
def upperCaseS(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.S])
    
def lowerCaseT(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.T])
    
def upperCaseT(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.T])
        
def lowerCaseU(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.U])
    
def upperCaseU(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.U])
        
def lowerCaseV(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.V])
    
def upperCaseV(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.V])
        
def lowerCaseW(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.W])
    
def upperCaseW(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.W])
        
def lowerCaseX(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.X])
    
def upperCaseX(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.X])
        
def lowerCaseY(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.Y])
    
def upperCaseY(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.Y])
        
def lowerCaseZ(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.Z])
    
def upperCaseZ(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.Z])
    
def number1(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.N1])
    
def exclamationMark(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.N1])
    
def number2(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.N2])
    
def quotationMark(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.N2])
    
def number3(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.N3])
    
def poundSign(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.N3])
    
def number4(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.N4])
    
def dollarSign(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.N4])
    
def number5(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.N5])
    
def percentSign(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.N5])
    
def number6(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.N6])
    
def caret(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.N6])
    
def number7(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.N7])
    
def ampersand(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.N7])
    
def number8(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.N8])
    
def asterisk(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.N8])
    
def number9(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.N9])
    
def leftBracket(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.N9])
    
def number0(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.N0])
    
def rightBracket(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.N0])
    
def enter(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.ENTER])
    
def escape(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.ESCAPE])
    
def backspace(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.BACKSPACE])
    
def tab(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.TAB])
    
def space(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.SPACE])
    
def minus(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.MINUS])
    
def underscore(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.MINUS])
    
def equal(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.EQUAL])
    
def plus(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.EQUAL])
    
def leftSquareBracket(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.OPEN_BRACKET])
    
def rightSquareBracket(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.CLOSE_BRACKET])
    
def leftCurlyBracket(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.OPEN_BRACKET])
    
def rightCurlyBracket(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.CLOSE_BRACKET])
    
def backslash(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.BACKSLASH])
    
def pipe(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.BACKSLASH])
    
def hashtag(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.HASH])
    
def tilde(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.HASH])
    
def semicolon(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.SEMICOLON])
    
def colon(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.SEMICOLON])
    
def quote(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.QUOTE])
    
def atSign(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.QUOTE])
    
def backtick(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.GRAVE])
    
def negation(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.GRAVE])
    
def comma(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.COMMA])
    
def leftAngleBracket(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.COMMA])
    
def fullstop(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.DOT])
    
def rightAngleBracket(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.DOT])
    
def forwardSlash(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.SLASH])
    
def questionMark(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT, KeyCode.SLASH])
    
def capsLock(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.CAPS_LOCK])
     
def function1(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.F1])
    
def function2(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.F2])
    
def function3(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.F3])
    
def function4(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.F4])
    
def function5(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.F5])
    
def function6(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.F6])
    
def function7(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.F7])
    
def function8(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.F8])
    
def function9(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.F9])
    
def function10(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.F10])
    
def function11(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.F11])
    
def function12(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.F12])
    
def scrollLock(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.SCROLL_LOCK])
    
def pause(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.PAUSE])
    
def insert(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.INSERT])
    
def delete(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.DELETE])

def home(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.HOME])
    
def end(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.END])
    
def pageUp(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.PAGEUP])
    
def pageDown(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.PAGEDOWN])
    
def up(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.UP])
    
def down(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.DOWN])
    
def left(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT])
    
def right(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.RIGHT])
    
def numLock(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.KP_NUM_LOCK])
    
def divide(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.KP_DIVIDE])
    
def multiply(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.KP_AT])
        
def subtract(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.KP_MINUS])
    
def add(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.KP_PLUS])
    
def leftCtrl(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_CTRL])
    
def rightCtrl(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.RIGHT_CTRL])
    
def leftShift(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_SHIFT])
    
def rightShift(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.RIGHT_SHIFT])

def leftAlt(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_ALT])
    
def rightAlt(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.RIGHT_ALT])

def leftUi(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.LEFT_UI])
    
def rightUi(keyboard, consumer, mouse):
    keyboard.send_keys([KeyCode.RIGHT_UI])
import pyautogui as pya
import time
time.sleep(1.5)

def textboxMaker():
    all_textboxes = list(pya.locateAllOnScreen("pics/pipe.png", confidence = .88))
    counter = 0
    pya.moveTo(all_textboxes[counter])
    pya.moveRel(-78, -19)
    pya.click()
    pya.dragRel(80,20, .5)
    time.sleep(.5)
    pya.moveTo(pya.locateCenterOnScreen("pics/height.png",grayscale = True, confidence = .8))
    pya.moveRel(-40,0)
    pya.click()
    pya.press("backspace")
    pya.press("backspace")
    pya.press("backspace")
    pya.write("14")
    pya.moveTo(pya.locateCenterOnScreen("pics/width.png", confidence = .8))
    pya.moveRel(-40,0)
    pya.click()
    pya.press("backspace")
    pya.press("backspace")
    pya.press("backspace")
    pya.write("60")
    pya.moveTo(pya.locateOnScreen("ok.png", confidence = .8))
    pya.click()
    for textboxes in all_textboxes:
        print(textboxes)
        textboxMaker()
        counter += 1
        

    

textboxMaker()
    
    
    



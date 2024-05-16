import pyautogui as pya
import time
import pyscreeze
time.sleep(2)


def textbox_maker():
    all_textboxes = list(pya.locateAllOnScreen("pics/target.png", confidence=.86))  # set confidence here

    textbox = all_textboxes[0]
    height = textbox.height
    width = textbox.width

    pya.moveTo(textbox.left + 2, textbox.top + 2)
    pya.click()
    pya.dragTo(textbox.left + width, textbox.top + height, 3, pya.easeOutQuad)
    # set over or under shoot above
    time.sleep(.5)

    pya.moveTo(pya.locateOnScreen("pics/ok.png", confidence=.7))
    pya.click()
    for textboxes in all_textboxes:
        print(textboxes)
        textbox_maker()


attempts = 0
while attempts < 20:
    try:
        textbox_maker()
    except pyscreeze.ImageNotFoundException:
        pya.scroll(-200)
        attempts += 1
        print("Attempt number: "+ str(attempts) + " \nWill quit after 20 failed attempts")
        time.sleep(1)
    except pya.ImageNotFoundException:
        pya.scroll(-200)
        attempts += 1
        print("Attempt number: " + str(attempts) + " \nWill quit after 20 failed attempts")
        time.sleep(1)
    except pya.FailSafeException:
        print("fail safe was triggered.")

    
    



import pyautogui as pya
from time import sleep
from pyscreeze import ImageNotFoundException
while True:
    checkbox = pya.locateOnScreen(r"C:/Users/hmetzger/OneDrive - Core Mechanical Services, INC/Desktop/useful scripts/checkbox.png", confidence = .9)
    print(checkbox)
    pya.moveTo(checkbox[0] - 5, checkbox[1])
    pya.click()
    pya.drag(checkbox[2] + 15,checkbox[3] + 17, 1.2)
    sleep(.5)   
    ok = pya.locateCenterOnScreen(r"C:\Users\hmetzger\OneDrive - Core Mechanical Services, INC\Desktop\useful scripts\ok.png", confidence = .8)
    pya.moveTo(ok)
    sleep(.5)
    pya.click()
    pya.scroll(-190)
    pya.moveTo(1500, 200)
    sleep(.2)
    pya.click()
    input("press enter to continue")
    # zoom 2867 % 
    



            
                

            
       
        
       




        
    
    

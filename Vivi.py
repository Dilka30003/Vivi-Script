from pyautogui import press, typewrite, hotkey
import keyboard
from keyboard import press
import time

x = 0

#time.sleep(5)
 
while x < 10000:
    keyboard.wait('esc')
    for i in range(0, 100):
        y = str(x).zfill(4)

    #    print(y)
    #    typewrite(y)
    #    hotkey('enter')
    #    hotkey('backspace')
    #    hotkey('backspace')
    #    hotkey('backspace')
    #    hotkey('backspace')
        keyboard.write(y)
        time.sleep(0.001)
        hotkey('enter')
        time.sleep(0.001)

        press('backspace')
        time.sleep(0.001)
        press('backspace')
        time.sleep(0.001)
        press('backspace')
        time.sleep(0.001)
        press('backspace')
        time.sleep(0.001)
        press('backspace')
        time.sleep(0.001)
        press('backspace')

        x = x + 1
        time.sleep(0.05)
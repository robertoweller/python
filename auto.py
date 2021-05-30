import pyautogui
from time import sleep

def click():
    pyautogui.click(x=654, y=148)
    sleep(.5)
    pyautogui.click(x=629, y=233)
# pyautogui.hotkey('ctrl', 'v')
# pyautogui.hotkey('enter')

def tab():
    pyautogui.keyDown('alt') 
    pyautogui.keyDown('tab')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('tab')

sleep(2)

for i in range(1434):
    click()
    tab()
    pyautogui.hotkey('ctrl', 'v')
    sleep(.1)
    pyautogui.hotkey('enter')
    tab()
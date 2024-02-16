import pyautogui
import time

while True:
    time.sleep(1)
    pyautogui.typewrite('I Luv You.')
    pyautogui.press('enter')
    
    
# -------------------
# to send 100 times

# for _ in range(100):
#     time.sleep(1)
#     pyautogui.typewrite('I Luv You.')
#     pyautogui.press('enter')

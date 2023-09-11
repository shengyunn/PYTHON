import pyautogui as ctrl
import time
ctrl.hotkey('win','i')
time.sleep(0.5)
ctrl.press('enter')
ctrl.typewrite('1i cl4')#search dial-up network settings 
ctrl.press('enter')
time.sleep(0.5)
ctrl.press('enter')
ctrl.press('tab')
ctrl.press('enter')
ctrl.hotkey('alt','F4')
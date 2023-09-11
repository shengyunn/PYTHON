import pyautogui as ctrl
import sys
import time


for i in range(60):
    print(ctrl.position())
    time.sleep(0.5)
    if ctrl.mouseDown(button='right'):
        print("右鍵被點擊，程式結束。")
        break   


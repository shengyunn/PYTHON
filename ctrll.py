import pyautogui
import keyboard

# 重複直到按下空白鍵
while True:
    pyautogui.moveTo(-2232, 404)
    pyautogui.click()
    pyautogui.moveTo(-970, 458)
    pyautogui.dragTo(-1630, 200, 1, button='left')
    pyautogui.press('enter')
    pyautogui.moveTo(-1246, 340)
    pyautogui.dragTo(-1109, 344, 1, button='left')

    pyautogui.moveTo(-2228, 41)
    pyautogui.click()
    pyautogui.press('enter')
    # 檢查是否按下空白鍵
    if keyboard.is_pressed('esc'):
        break


# pyautogui.moveTo(-1882, 534) 
# pyautogui.click()
# pyautogui.moveTo(-1666, 140) 
# pyautogui.click()
# pyautogui.moveTo(-976, 355) 
# pyautogui.click()
# print(pyautogui.position())

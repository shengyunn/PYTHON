import keyboard
import pyautogui
import threading
import time

exit_program = False  # 新增一個變數來控制是否退出程式

def print_position():
    for _ in range(30):
        print(pyautogui.position())
        time.sleep(0.5)
        if exit_program:  # 檢查是否需要退出程式
            break

def on_esc_press(e):
    global exit_program  # 告訴Python我們要使用全局變數
    if e.name == 'esc':
        print("程式結束")
        exit_program = True  # 設置退出程式的標誌
        keyboard.unhook_all()  # 解除鍵盤監聽

keyboard.on_press(on_esc_press)

# 啟動一個新的線程來執行print_position函數
thread = threading.Thread(target=print_position)
thread.start()

# 等待副線程執行完成後再退出
thread.join()

# 程式會在此退出

import pyautogui
import time

# 取得螢幕寬度和高度
screen_width, screen_height = pyautogui.size()

# 設定開始時間
start_time = time.time()

# 持續運行直到達到指定時間
while time.time() - start_time < 30:
    # 取得鼠標位置
    x, y = pyautogui.position()

    # 取得指定位置的 RGB 值
    pixel_color = pyautogui.pixel(x, y)

    # 輸出 RGB 值
    print(f"在座標 ({x}, {y}) 的像素顏色為 {pixel_color}")

    # 暫停一段時間（避免過度消耗系統資源）
    time.sleep(0.1)

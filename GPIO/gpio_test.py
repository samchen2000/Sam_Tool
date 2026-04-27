import tkinter as tk
from tkinter import ttk
import RPi.GPIO as GPIO

# 設定 GPIO 輸出位
GPIO_PIN = 17  # 可以根據你的實際 GPIO 引號修改

# 建立 GUI 窗口
root = tk.Tk()
root.title("GPIO Control")

# 建立 GPIO 控制器
GPIO.setmode(GPIO.BCM)  # 使用 BCM 模式，更常見
GPIO.setup(GPIO_PIN, GPIO.OUT)
# 建立一個簡單的 按鍵事件處理器
def on_key_pressed():
    print("按鍵被按下!")
    # 這裡可以添加你想要的處理邏輯
    # 例如：
    # GPIO.output(GPIO_PIN, True)  # 實際設定 GPIO 輸出
    #  或者，執行一些其他操作
    # 比如更新GUI，顯示訊息等
    GPIO.output(GPIO_PIN, GPIO.HIGH)

def on_key_released():
    print("按鍵鬆開!")
    # 這裡可以添加你想要的處理邏輯
    # 比如：
    # GPIO.output(GPIO_PIN, False)  # 實際設定 GPIO 輸出
    GPIO.output(GPIO_PIN, GPIO.LOW)

# 建立一個按鍵列表，用於控制 GPIO 的狀態
key_list = []
for i in range(7):
    key_list.append(str(i))

# 建立一個按鈕，用於按下按鍵
button = tk.Button(root, text="按下按鍵", command=on_key_pressed)
button.pack(pady=10)

# 建立一個按鈕，用於鬆開按鍵
button = tk.Button(root, text="鬆開按鍵", command=on_key_released)
button.pack(pady=10)


# 建立一個用於偵測按鍵事件的圓圈
circle = tk.Canvas(root, width=10, height=10, bg="white")
circle.pack(pady=10)

# 循環執行事件處理器
root.bind("<KeyRelease>", on_key_released)  # 每次按鍵鬆開時，觸發
on_key_released
root.bind("<Return>", on_key_pressed) # 每次按下回車鍵時，觸發
on_key_pressed


# 執行メイン循環
root.mainloop()

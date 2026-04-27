"""gpio_test1.py

簡單的 GPIO 測試程式。這個版本會嘗試載入 RPi.GPIO，
如果在非 Raspberry Pi 或無法存取 /dev/mem 時，會自動切換到 MockGPIO
以便在開發機上也能執行並觀察模擬輸出。

使用方式:
    python3 gpio_test1.py

按 Ctrl+C 結束程式。
"""

import time
import sys

# 嘗試載入真實的 RPi.GPIO，若失敗則提供一個簡易模擬實作
hardware_gpio = True
try:
    import RPi.GPIO as GPIO
except (RuntimeError, ModuleNotFoundError) as e:
    hardware_gpio = False
    print("[WARN] RPi.GPIO 無法載入：{}\n      使用 MockGPIO 以便在非 Pi 環境測試".format(e))

    class MockGPIO:
        BCM = 'BCM'
        BOARD = 'BOARD'
        OUT = 'OUT'
        IN = 'IN'
        HIGH = 1
        LOW = 0
        PUD_UP = 'PUD_UP'

        def __init__(self):
            self._mode = None
            self._states = {}

        def setwarnings(self, flag):
            pass

        def setmode(self, mode):
            self._mode = mode
            print(f"[MOCKGPIO] setmode({mode})")

        def setup(self, pin, mode, pull_up_down=None):
            self._states[pin] = self.LOW
            print(f"[MOCKGPIO] setup(pin={pin}, mode={mode}, pull_up_down={pull_up_down})")

        def output(self, pin, value):
            self._states[pin] = value
            level = 'HIGH' if value else 'LOW'
            print(f"[MOCKGPIO] output(pin={pin}) -> {level}")

        def cleanup(self):
            print("[MOCKGPIO] cleanup() 清理完成")
            self._states.clear()

    GPIO = MockGPIO()


def main():
    # 設定 GPIO 模式 (BCM 或 BOARD)
    try:
        GPIO.setmode(GPIO.BCM)  # 使用 Broadcom SOC channel number
    except Exception as e:
        # 若在某些情況下 setmode 失敗，顯示警告並繼續（mock 模式會走到這裡）
        print(f"[WARN] GPIO.setmode 例外: {e}")

    # 設定 GPIO 引腳編號 (這裡以 GPIO 17 , 27 為例)
    led_pin = 17
    led_pin_1 = 27
    led_pin_2 = 22
    led_pin_3 = 26
    
    #三色LED 使用的GPIO
    led_pin_4 = 16
    led_pin_5 = 20

    try:
        GPIO.setup(led_pin, GPIO.OUT)
        GPIO.setup(led_pin_1, GPIO.OUT)
        GPIO.setup(led_pin_2, GPIO.OUT)
        GPIO.setup(led_pin_3, GPIO.OUT)
        GPIO.setup(led_pin_4, GPIO.OUT)
        GPIO.setup(led_pin_5, GPIO.OUT)
    except Exception as e:
        print(f"[ERROR] 設定 GPIO 失敗: {e}")
        if hardware_gpio:
            print("請確認程式在 Raspberry Pi 上執行，且有足夠權限存取 /dev/mem 或使用 pigpio 等替代方案。")
        # 若 setup 失敗但我們使用 mock，繼續執行以便觀察模擬輸出

    print("按 Ctrl+C 終止程式")
    try:
        while True:
            # 開啟 LED (設定為高電平)
            GPIO.output(led_pin, GPIO.HIGH)
            GPIO.output(led_pin_1, GPIO.LOW)
            GPIO.output(led_pin_2, GPIO.LOW)
            GPIO.output(led_pin_3, GPIO.LOW)
            GPIO.output(led_pin_4, GPIO.LOW)
            GPIO.output(led_pin_5, GPIO.LOW)
            print("GPIO_17_亮")
            time.sleep(0.2)

            # 關閉 LED (設定為低電平)
            GPIO.output(led_pin_1, GPIO.HIGH)
            GPIO.output(led_pin, GPIO.LOW)
            GPIO.output(led_pin_2, GPIO.LOW)
            GPIO.output(led_pin_3, GPIO.LOW)
            print("GPIO_22_亮")
            time.sleep(0.2)
            
            # 關閉 LED (設定為低電平)
            GPIO.output(led_pin_2, GPIO.HIGH)
            GPIO.output(led_pin_3, GPIO.LOW)
            GPIO.output(led_pin, GPIO.LOW)
            GPIO.output(led_pin_1, GPIO.LOW)
            print("GPIO_22_亮")
            time.sleep(0.2)
            
            # 關閉 LED (設定為低電平)
            GPIO.output(led_pin_3, GPIO.HIGH)
            GPIO.output(led_pin, GPIO.LOW)
            GPIO.output(led_pin_1, GPIO.LOW)
            GPIO.output(led_pin_2, GPIO.LOW)
            print("GPIO_18_亮")
            time.sleep(0.2)
            
            # 關閉 LED (設定為低電平)
            GPIO.output(led_pin_4, GPIO.HIGH)
            GPIO.output(led_pin_5, GPIO.LOW)
            print("雙色燈(紅)_亮")
            time.sleep(0.2)
            GPIO.output(led_pin_4, GPIO.LOW)
            GPIO.output(led_pin_5, GPIO.HIGH)
            print("雙色燈(綠)_亮")
            time.sleep(0.2)
            GPIO.output(led_pin_4, GPIO.HIGH)
            GPIO.output(led_pin_5, GPIO.HIGH)
            print("雙色燈(橙)_亮")
            time.sleep(0.2)
            
            # LED 一起亮
            GPIO.output(led_pin, GPIO.HIGH)
            GPIO.output(led_pin_1, GPIO.HIGH)
            GPIO.output(led_pin_2, GPIO.HIGH)
            GPIO.output(led_pin_3, GPIO.HIGH)
            print("LED 一起亮")
            time.sleep(0.2)
            
            # LED 一起滅
            GPIO.output(led_pin, GPIO.LOW)
            GPIO.output(led_pin_1, GPIO.LOW)
            GPIO.output(led_pin_2, GPIO.LOW)
            GPIO.output(led_pin_3, GPIO.LOW)
            print("LED 一起滅")
            time.sleep(0.2)
            
    except KeyboardInterrupt:
        # 程式中斷 (例如按下 Ctrl+C)
        try:
            GPIO.output(led_pin, GPIO.LOW)
            GPIO.output(led_pin_1, GPIO.LOW)
            GPIO.output(led_pin_2, GPIO.LOW)
            GPIO.output(led_pin_3, GPIO.LOW)
        except Exception:
            pass
        print("程式終止")

    finally:
        # 在程式結束前，重設所有 GPIO 引腳狀態
        try:
            GPIO.cleanup()
        except Exception:
            pass
        print("GPIO 清理完成")


if __name__ == '__main__':
    main()

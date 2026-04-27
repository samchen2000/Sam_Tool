import RPi.GPIO as GPIO
import time

# 設定 GPIO 模式
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# 設定 Trig 和 Echo 的 GPIO 接腳
Trig = 23
Echo = 24

# 設定 GPIO 模式
GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)

def measure_distance():
    # 1. 觸發超音波發射
    GPIO.output(Trig, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(Trig, GPIO.LOW)

    # 2. 記錄 Echo 訊號的開始時間（加入超時保護）
    timeout = time.time() + 0.1  # 100ms 超時
    start_time = time.time()
    while GPIO.input(Echo) == 0:
        if time.time() > timeout:
            return None
        start_time = time.time()

    # 3. 記錄 Echo 訊號的結束時間（加入超時保護）
    timeout = time.time() + 0.1  # 100ms 超時
    stop_time = time.time()
    while GPIO.input(Echo) == 1:
        if time.time() > timeout:
            return None
        stop_time = time.time()

    # 4. 計算時間差
    time_diff = stop_time - start_time

    # 5. 計算距離 (公分) = (時間差 × 聲速) / 2
    distance = (time_diff * 34300) / 2
    
    # 6. 驗證距離是否在合理範圍內 (2cm - 400cm)
    if 2 <= distance <= 400:
        return distance
    return None

print("超音波測距儀啟動...")

try:
    while True:
        distance = measure_distance()
        if distance is not None:
            print(f"距離: {distance:.1f} 公分")
        else:
            print("無法測量距離，請檢查感測器連接")
        
        time.sleep(0.1)  # 延遲 100ms
except KeyboardInterrupt:
    print("\n程式結束")
finally:
    GPIO.cleanup()  # 清理 GPIO 設定
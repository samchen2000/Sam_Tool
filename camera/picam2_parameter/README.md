## picam2 參數主要涉及相機的配置，包括圖像分辨率、幀率、曝光、對焦等。 這些參數可以通過 picam2.start_and_capture_video_stream()、picam2.start_and_capture_image() 等函數來設置和調整，以滿足不同的應用需求。 具體來說，picam2 允許使用者控制以下幾個關鍵參數：
### 1. 圖像尺寸(Resolution):
- 可以設置錄製視頻或拍攝照片的分辨率，例如1920x1080 (1080p), 1280x720 (720p) 等。
- 示例：config["main"]["size"] = (1920, 1080)
### 2. 幀率(Frame Rate):
- 設定錄製視頻的幀率，例如30fps (每秒30幀)。
- 示例：config["main"]["framerate"] = 30
### 3. 曝光(Exposure):
- 控制圖像的亮度，可以自動曝光(Auto Exposure) 或手動曝光。
- 自動曝光模式下，picam2 會根據環境光線自動調整曝光時間。
- 手動曝光模式下，可以通過 config["controls"]["ExposureTime"] 設置具體的曝光時間(單位: 微秒)。
- 示例(自動曝光): config["controls"]["AeEnable"] = True
- 示例(手動曝光): config["controls"]["ExposureTime"] = 10000 (10 毫秒)
### 4. 對焦(Focus):
- picam2 默認使用自動對焦(Auto Focus)，但也可以設置為手動對焦。
- 手動對焦模式下，可以通過 config["controls"]["LensPosition"] 調整鏡頭位置，以達到不同的對焦距離。
- 示例(自動對焦): config["controls"]["AfMode"] = 0
- 示例(手動對焦): config["controls"]["LensPosition"] = 1.0 (具體數值根據鏡頭和校準情況而定)
### 5. 其它參數:
- picam2 還支持調整其他參數，例如：
>- config["controls"]["AnalogueGain"]: 模擬增益，影響圖像的亮度。
>- config["controls"]["ColourGains"]: 色彩增益，調整圖像的顏色。
>- config["controls"]["Sharpness"]: 銳度，調整圖像的清晰度。
>- config["controls"]["Contrast"]: 對比度，調整圖像的明暗對比。
>- config["controls"]["Saturation"]: 飽和度，調整圖像的色彩鮮豔程度。
>- config["controls"]["BufferCount"]: 緩衝區大小，影響視頻錄製的流暢度。
>- config["controls"]["FrameDuration"]: 幀持續時間，控制每幀的顯示時間。
### 如何使用這些參數:
picam2 通過 config 字典來配置相機。 使用者可以根據自己的需求，修改這個字典中的相關參數，然後將其應用於相機。 \
例如，要設置分辨率為1920x1080，幀率為30fps，曝光時間為10 毫秒，並且使用自動對焦，可以使用以下代碼：
```
from picamera2 import Picamera2

picam2 = Picamera2()
config = picam2.create_video_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
picam2.configure(config)

# 設置參數
config["controls"]["ExposureTime"] = 10000  # 10 毫秒
config["controls"]["AeEnable"] = True  # 自動曝光
config["controls"]["AfMode"] = 0  # 自動對焦

picam2.start()
```
總結來說，picam2 提供了豐富的參數，允許使用者根據實際情況靈活調整相機的配置，以達到最佳的圖像或視頻效果。
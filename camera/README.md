MIPI Camera GUI (Raspberry Pi 5)

簡介
----
這是使用 Python + OpenCV + Tkinter 製作的簡易 GUI 範例，支援 Raspberry Pi 5 與 MIPI CSI 相機。

安裝相依
----
建議使用虛擬環境後安裝：

```bash
pip install -r requirements.txt
```

執行
----

```bash
python3 mipi_camera_gui.py
```

說明
----
- 右側面板可透過滑桿或 +/- 微調：亮度、對比、飽和、色相、R/G/B 倍率。
- Snapshot 會在執行目錄存成 `snapshot_<ts>.png`。

注意事項
----
- 確保啟用 camera driver（libcamera / v4l2 支援），Raspberry Pi OS 上需先透過 `raspi-config` 或相關設定啟用 MIPI 相機。
- 在某些系統上可能需使用 `sudo` 執行以取得相機權限。
## 如何將相機模組連接到 Raspberry Pi 5？
aspberry Pi 5 提供了全新的性能升級與功能擴展，其中相機模組是一個極具創造力的工具，讓使用者可以輕鬆實現影像處理、AI 視覺等應用。本文將一步步教你如何將相機模組連接到 Raspberry Pi 5 並進行測試。
### 準備工作
> Raspberry Pi 5 \
> 官方相機模組（建議使用 Camera Module 3）\
> MicroSD 記憶卡（安裝 Raspberry Pi OS）\
> 顯示器與鍵盤/滑鼠 \
> 相機模組連接線 \
> 5V/USB-C 電源 \

### 步驟一：檢查硬體連接
Raspberry Pi 5 提供了兩個 CSI 接口（CAM1 和 CAM2）。確保相機模組的連接線金屬觸點面朝接口內部，並插入後鎖緊接頭。
### 更新與安裝驅動程式
Raspberry Pi 5 的相機模組使用全新的 libcamera 驅動架構，預設隨系統提供。如果需要，請執行以下指令更新系統並安裝相機應用：

>> sudo apt update \
>> sudo apt full-upgrade \
>> sudo apt install -y libcamera-apps
### 步驟三：測試相機模組
#### 預覽畫面：
>> libcamera-hello
#### 拍攝照片：
>> libcamera-jpeg -o test.jpg
#### 錄製影片：
>> libcamera-vid -t 10000 -o test.h264 \

如果能成功看到預覽畫面或生成檔案，表示安裝成功！

### 進階應用：雙相機功能
Raspberry Pi 5 支援同時連接兩個相機模組，你可以分別插入 CAM1 和 CAM2 接口，並使用以下指令測試每個相機：
#### 第一個相機：
>> libcamera-hello --camera 0 
#### 第二個相機：
>> libcamera-hello --camera 1

# 目前買的 image sensor module : OV5647



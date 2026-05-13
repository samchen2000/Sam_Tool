# Raspberry Pi 上開機自動執行 Python 程式
## 最常見且穩定的方法是使用 Systemd 服務（適合背景程式）或修改 LXDE autostart（適合需要桌面環境的 GUI 程式）。
## 方法一：使用 Systemd 服務（推薦，適合背景常駐程式）
### 1. 建立 Service 檔案：
```
sudo nano /lib/systemd/system/myscript.service
```
### 2. 寫入以下內容（請自行修改路徑與用戶名）：  
```ini
[Unit]
Description=My Python Script
After=multi-user.target

[Service]
Type=idle
User=pi
ExecStart=/usr/bin/python3 /home/pi/your_script.py
Restart=always

[Install]
WantedBy=multi-user.target
```
### 3. 啟用服務：
```bash
sudo systemctl daemon-reload
sudo systemctl enable myscript.service
sudo reboot
```
## 方法二：修改 LXDE autostart（適合圖形介面 GUI）
#### 1. 編輯 autostart 檔案：
```
nano /home/pi/.config/lxsession/LXDE-pi/autostart
```
#### 2. 在檔案末尾添加：
```
@/usr/bin/python3 /home/pi/your_script.py
```
(如果要開 terminal 執行：@lxterminal -e python3 /home/pi/your_script.py)
### 3. 方法三：
- #### 1. 使用 rc.local（傳統方法）
編輯 rc.local：
```
sudo nano /etc/rc.local
```
- #### 2. 在 exit 0 前面添加：
```
/usr/bin/python3 /home/pi/your_script.py &
```
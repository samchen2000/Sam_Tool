# 如何在raspberry pi5 建立一個 web UI 介面的框架,可以透過IP 進入到 raspberry 的WEB介面.

要在 Raspberry Pi 5 上建立一個可以透過 IP 存取的 Web UI，最推薦的方式是使用 Python 的 Web 框架。考慮到 RPi 5 的強大效能（四核心、更快的存取速度），運行這些框架會非常流暢。

以下為你介紹三種最主流的方案，從「最簡單」到「最彈性」排列：
## 1. 事前準備：獲取 Raspberry Pi 的 IP
在開始之前，你需要知道 RPi 的區域網路 IP 位址。在終端機輸入：
```Bash
hostname -I
```
這會顯示類似 **192.168.1.125** 的數字。
## 2. 方案一：Streamlit (最快建立介面)
如果你想在幾分鐘內寫出一個漂亮的控制面板或數據看板，Streamlit 是首選。它不需要寫任何 HTML/CSS。

## 安裝步驟教學
- ### 1. 建立虛擬環境 (RPi OS 建議做法)：

```Bash
mkdir my_web_app && cd my_web_app
python -m venv venv
source venv/bin/activate
```
- ### 2. 安裝 Streamlit：

```Bash
pip install streamlit
```
- ### 3. 編寫程式碼 (app.py)：
```Python
import streamlit as st
st.title("Raspberry Pi 5 控制中心")
st.write("這是透過 Streamlit 建立的 Web UI。")
if st.button("點擊我"):
    st.balloons()
    st.success("按鈕已被觸發！")
 ```
- 4. 執行並開放存取：
```Bash
streamlit run app.py --server.address 0.0.0.0
```
注意：--server.address 0.0.0.0 非常關鍵，這表示允許區網內的所有裝置存取。
## 3. 方案二：Gradio (適合簡單互動與 AI 模型)
既然你之前問過 Gradio，這也是一個極佳的選擇，特別適合用來控制 RPi 的硬體（如 GPIO、相機）。

- ### 1. 安裝與執行
安裝：```pip install gradio```

編寫 app.py：

```Python
import gradio as gr
import os

def get_system_info():
    return os.popen("vcgencmd measure_temp").readline()

demo = gr.Interface(fn=get_system_info, inputs=None, outputs="text", title="RPi 溫度監控")

# server_name="0.0.0.0" 是對外開放的關鍵
demo.launch(server_name="0.0.0.0", server_port=7860)
```
## 4. 方案三：Flask (最經典、高度自訂)
如果你想要建立一個標準的網站（有 HTML、CSS、多個頁面），Flask 是工業標準。

### 基本框架結構
- 1. 安裝：pip install flask

- 2. 編寫 app.py：

```Python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>歡迎來到 Raspberry Pi 5 伺服器</h1>"

if __name__ == '__main__':
    # host='0.0.0.0' 允許透過 IP 進入
    app.run(debug=True, host='0.0.0.0', port=5000)
````    
## 如何從另一台電腦進入？
確保你的電腦與 Raspberry Pi 連接在同一個 Wi-Fi 或路由器下。

在電腦的瀏覽器網址列輸入：

Streamlit: http://192.168.x.x:8501

Gradio: http://192.168.x.x:7860

Flask: http://192.168.x.x:5000
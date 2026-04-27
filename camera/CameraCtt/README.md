## 程式說明
### alsc_only.py
1. 這段程式碼是一個用於鏡頭陰影校正 (ALS, Auto Lens Shading Correction) 的調校工具
2.  -i：校準影像的目錄。\
    -o：輸出的 JSON 檔案名稱。\
    可選參數：\
    -t：目標平台，預設為 'vc4'，可選 'pisp' 或 'vc4'。\
    -c：CTT 的設定檔，若未提供則使用預設參數。\
    -l：輸出日誌檔案名稱，若未提供則使用 'ctt_log.txt'。\
最後使用 quit(0) 結束程式。
### cac_only.py
1. 這段 Python 程式碼是一個工具程式，用於調整相機模組的「色差校正」（Chromatic Aberration Correction, CAC）。它的目的是從相機拍攝的 .dng 格式的圖像中計算色差，並生成一個用於校正的 LUT（查找表），以便將其整合到相機的調整檔案中。
2. 
### colors.py
1. 這段 Python 程式碼的功能是將 RGB 色彩空間的顏色轉換為 LAB 色彩空間。LAB 色彩空間是一種基於人類視覺模型的色彩空間，常用於影像處理和色彩分析。
### convert_tuning.py
1. 這段 Python 程式碼是一個用於將 Raspberry Pi 相機的調校檔案從版本 1.0 轉換為版本 2.0 的工具。
### ctt.py
1. 這段程式碼是一個用於相機校準的工具，主要目的是進行相機的色彩校正和其他相關校準操作。
### ctt.alsc.py
1. 這段程式碼是一個用於相機自動鏡頭陰影校正（ALSC）的工具。它的主要功能是對一組圖像進行ALSC校準。
### ctt.awb.py
1. 這段程式碼的目的是用於自動白平衡（AWB，Auto White Balance）調整，特別是針對相機的色彩曲線進行調整。
### ctt_cac.py
### ctt_ccm.py
### ctt_config_example.json
### ctt_dots_locator.py
### ctt_geq.py
### ctt_image_load.py
### ctt_noise.py
### ctt_pisp.py
1. 這段程式碼是一個用於樹莓派（Raspberry Pi）相機調校工具（Camera Tuning Tool, CTT）的 Python 腳本，主要是定義了相機的各種參數調校配置，並以 JSON 格式儲存這些設定。
### ctt_pretty_print_json.py
1. 這段程式碼是一個用於美化（pretty print）Raspberry Pi 相機調校配置 JSON 檔案的 Python 腳本。
### ctt_ransac.py
1. 這段程式碼的功能是為了生成一個與 Macbeth 色卡（Macbeth ColorChecker）相關的幾何結構，這些結構可以用於 RANSAC（隨機採樣一致性，RANdom SAmple Consensus）演算法來進行色卡定位。
### ctt_ref.pgm
### ctt_tools.py
1. 這段程式碼是一個用於圖像處理和參數解析的工具程式碼。
### ctt_vc4.py
1. 這段程式碼是一個用於設定 Raspberry Pi 相機調校工具（Camera Tuning Tool, 簡稱 CTT）的 Python 程式片段，主要針對 VC4 平台（VideoCore IV）進行調校。
### ctt_visualise.py
1. 這段程式碼的主要功能是產生一張「虛擬 Macbeth 色卡」的圖片，用於比較優化矩陣（new_rgb）與非優化矩陣（original_rgb）的顏色差異。

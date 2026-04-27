## ADB 指令
ADB (Android Debug Bridge) 是一種多功能的命令行工具，用於與Android 設備進行通信，進行除錯、應用程式安裝、檔案傳輸等操作。 它包含客戶端、伺服器和守護進程(daemon) 三個部分。\
### 以下是一些常用的ADB 指令：
1. 設備管理:
>adb devices: 列出所有已連接的Android 設備。 \
>adb connect <device_ip_address>[:port]: 通過Wi-Fi 連接到指定IP 地址的設備，可選端口。 \
>adb disconnect [<device_ip_address>[:port]]: 斷開與指定設備的連接。 \
>adb -s <serial_number> command: 對指定的設備執行命令。 \
>adb remount: 重新掛載system 分區為可讀寫。 \
>adb root: 獲取root 權限(如果設備支持)。 \
>adb disable-verity: 禁用設備的分區驗證。 

2. 文件操作:
>adb push <local> <remote>: 將本地文件複製到設備。 \
>adb pull <remote> <local>: 從設備複製文件到本地。 \
>adb shell ls <path>: 列出設備指定路徑的文件和文件夾。 \
>adb shell rm <file_path>: 刪除設備上的文件。 \
>adb shell mkdir <directory_path>: 在設備上創建文件夾。 

3. 應用程式管理:
>adb install <apk_path>: 安裝APK 文件到設備。 \
>adb uninstall <package_name>: 卸載指定包名的應用程式。 \
>adb shell pm list packages: 列出所有已安裝的應用程式包名。 \
>adb shell am start -n <package_name>/<activity_name>: 啟動指定的應用程式活動。 \
>adb shell am force-stop <package_name>: 停止指定的應用程式。 \
>adb shell pm path <package_name>: 查看應用程式的安裝路徑。 

4. 日誌和除錯:
>adb logcat: 顯示設備的日誌。 \
>adb logcat -c: 清除日誌。 \
>adb logcat -d > log.txt: 將日誌輸出到本地文件。 \
>adb shell dumpsys battery: 查看設備的電池狀態。 \
>adb shell screenrecord /sdcard/video.mp4: 錄製設備屏幕。 

5. 其他:
>adb shell input keyevent <keycode>: 模擬按鍵事件。 \
>adb shell screencap -p /sdcard/screenshot.png: 截取設備屏幕截圖。 \
>adb shell getprop <property_name>: 獲取設備的系統屬性。 \
>adb shell setprop <property_name> <value>: 設置設備的系統屬性。 

6. 備註:
>在執行ADB 指令前，請確保已啟用USB 偵錯模式，並將設備通過USB 連接到電腦。 \
>有些指令需要root 權限才能執行。 \
ADB 指令的詳細說明可以參考官方文檔 \
 [Android Developers](https://developer.android.com/tools/adb?hl=zh-tw "參考文件")

## ADB 常用指令
1. 裝置連線 ``adb connect "裝置的ip"``

大家在開發時通常都是手機接 USB 與電腦連線，但如果測試機一多身邊的 USB 線不夠該怎麼辦才好呢? \
這時你可以透過 adb connect 的方式來做連線，不過再下這個指令前請先確認你的 5555 port 是否已經打開，如果沒有，輸入完指令會出現以下錯誤訊息: \

***unable to connect to 裝置的ip:5555: cannot connect to 裝置的ip:5555: 無法連線，因為目標電腦拒絕連線。 (10061)***

所以請先下指令 ``"adb tcpip 5555"`` \
之後再下 ``"adb connect "裝置的ip""`` 

2. **取得目前連線裝置清單 ``"adb devices"``**

3. **清除所有連線 ``"adb kill-server"``**

4. **指定特定裝置動作 ``"adb -s "裝置名稱" 動作指令"``**
如果目前同時連線的裝置有兩台或兩台以上，下指令時電腦沒辦法同時間對每個裝置做動作，所以必須指定某台裝置做動作。 \
此時我們先下 adb devices 列出所有連線的裝置名稱 \
接著下 adb -s "裝置名稱" 動作指令

    ***adb -s 10.10.35.128:5555 shell*** \
5. 安裝app ``adb install apk所在位置``
***adb install E:\Cindy\test.apk***
6. 移除app ``adb uninstall "packageName"``
***adb uninstall com.cindy.test***
7. 對裝置送KeyCode ``adb shell input keyevent "KeyCode"``
***adb shell input keyevent 3 (3為Home鍵的KeyCode)*** \
*KeyCode可參考以下網址：\
[Keycode](http://www.mail-archive.com/android-developers@googlegroups.com/msg14587.html"參考文件")
8. 用ADB指令傳送文字 ``adb shell input text "想輸入的文字"``
***adb shell input text "Cindy"*** \
Ps: 記得打雙引號 \
9. 重新開機 ``adb reboot``

10. 對特定app清除資料 ``adb shell pm clear "packageName"``
這個指令等同於：設定->應用程式->點選特定app->清除資料
***adb shell pm clear com.cindy.test***
11. 強制停止特定app adb shell am force-stop "packageName"
這個指令等同於：設定->應用程式->點選特定app->強制停止
***adb shell am force-stop com.cindy.test***
12. 開啟特定app ``adb shell am start -n "packageName"/".進入點Activity Name"`` \
***adb shell am start -n com.cindy.test/.MainActivity***
13. 顯示指令小幫手 ``adb help``
14. 將檔案丟到手機裡 ``adb push "檔案位置" "裝置裡目的地位置" ``\
如果未來大家有開發到系統級的app的話 就需要用push的方式把app丟到系統資料夾內喔
***adb push cindy.apk /system/app/***
15. 將檔案從裝置中拿出來 ``adb pull "檔案在裝置裡的位置" "目的地位置"`` \
***"adb pull /system/app/cindy.apk E:\Cindy\"*** 

那接下來就介紹幾個 Android 常用的 ADB Shell 指令囉 \
首先輸入指令 ``adb shell`` 進入 Shell 模式
1. 到指定路徑 ``cd "路徑位置"``
***cd /storage/sdcard0/Cindy***
2. 回該路徑上一層資料夾 ``cd ..``
3. 列出該資料夾中的檔案 ``ls`` or ``ls "資料夾位置"`` \
***ls /storage/sdcard0/Cindy***
4. 刪除檔案 ``rm "檔案名稱或位置"`` \
***rm Cindy.jpg*** \
***rm /storage/sdcard0/Cindy/Cindy.jpg***
5. 刪除資料夾 \
``rm -r "資料夾名稱或位置"`` or ``rmdir "資料夾名稱或位置"`` \
***rm -r Cindy*** \
***rm -r /storage/sdcard0/Cindy*** \
***rmdir Cindy*** \
***rmdir /storage/sdcard0/Cindy***
6. 新增資料夾 ``mkdir "資料夾名稱"`` \
***mkdir Cindy***
7. 閱讀文字檔 ``cat "文字檔或路徑"`` \
***cat cindy.txt*** \
***cat /storage/sdcard0/Cindy/cindy.txt***
8. 更改檔案權限 ``chmod 欲修改的權限 "檔案名稱或路徑"`` \
***chmod 644 cindy.txt***
9. 取得檔案MD5 ``md5sum "檔案名稱或路徑"`` \
***md5sum cindy.txt*** \
***md5sum /storage/sdcard0/Cindy/cindy.txt***
10. 取得系統資訊 ``getprop`` \
***getprop*** \
***or*** \
***getprop | grep sys // 只過濾出含有 sys 的資料*** \
11. 離開Shell模式 ``exit``

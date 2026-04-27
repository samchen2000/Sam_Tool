## 
要在VS Code中上傳代碼到GitHub，你需要先將本地專案初始化為Git倉庫，然後將本地倉庫與GitHub倉庫關聯，最後將本地修改推送到GitHub。 以下是詳細步驟：
1. 初始化本地Git倉庫:
•	在VS Code中，打開你的專案檔案夾。 \
•	打開終端（通常在“視圖”->“終端”中）。 \
•	輸入 git init 初始化一個新的Git倉庫。 \
•	輸入 git add . 暫存所有檔。 \
•	輸入 git commit -m "Initial commit" 提交暫存的檔，並添加提交資訊。 
2. 關聯本地倉庫與GitHub倉庫:
•	在GitHub上創建一個新的倉庫。 \
•	複製GitHub倉庫的URL。 \
•	在VS Code終端中，輸入 git remote add origin <your-repository-url>，替換 <your-repository-url> 為你的倉庫URL。
•	輸入 git branch -M main (或者 git branch -M master，如果你的GitHub倉庫使用master分支) 將當前分支重命名為main（或master）。
•	輸入 git push -u origin main (或者 git push -u origin master) 將本地倉庫推送到GitHub倉庫。
3. 日常同步代碼:
•	在VS Code中，對代碼進行修改。 \
•	打開終端，輸入 git add . 暫存所有修改。 \
•	輸入 git commit -m "Your commit message" 提交修改，並添加提交資訊。 \
•	輸入 git push 將修改推送到GitHub。


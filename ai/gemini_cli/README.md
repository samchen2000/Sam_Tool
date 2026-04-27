## Gemini CLI
這是一個開源的 AI 代理工具（AI Agent），讓你可以在  Windows 的終端機（命令提示字元）裡直接跟 Gemini AI 對話，請它幫你完成各種電腦任務。想要叫它檢查磁碟空間？幫你寫一個自動備份的小程式？甚至用 winget 安裝軟體？通通沒問題！ 免費軟體與共用軟體
##  1. 系統需求
  在安裝前，請確認您的環境符合以下條件：
   * Node.js： 必須安裝 v20.0.0 或更高版本。
   * 作業系統： 支援 macOS 15+、Windows 11 24H2+ 或 Ubuntu 20.04+（您的系統為 Linux，符合要求）。
   * 記憶體： 建議至少 4GB RAM，處理大型專案建議 16GB。
##  2. 安裝步驟
  您可以選擇以下任一方式安裝：

   * 全域安裝 (npm)：
```   
npm install -g @google/gemini-cli
```
   * 免安裝執行 (npx)：
      如果你只想嘗試，可以直接執行：
```
npx @google/gemini-cli
```
### 3. API 金鑰設定
  Gemini CLI 需要 API 金鑰才能運作：

   1. 取得金鑰： 前往 Google AI Studio (https://aistudio.google.com/app/apikey) 產生一組金鑰。
   2. 設定環境變數：
       * 在終端機執行：export GEMINI_API_KEY="您的金鑰內容"
   3. 永久保存設定：
      為了避免每次都要輸入，建議在您的家目錄建立設定檔：
       * 建立目錄：mkdir -p ~/.gemini
       * 建立檔案：nano ~/.gemini/.env
       * 內容寫入：GEMINI_API_KEY="您的金鑰內容"
   4. 啟動與認證：
      執行 gemini，並在選單中選擇 "Use Gemini API key"。
4. 常見錯誤與修正方式

  ┌───────────────────────┬────────────────────┬────────────────────────────────────────────────────────────────────────────────────┐
  │ 錯誤現象              │ 可能原因           │ 修正方式                                                                           │
  ├───────────────────────┼────────────────────┼────────────────────────────────────────────────────────────────────────────────────┤
  │ Command not found     │ npm 全域路徑未加入 │ 檢查 npm config get prefix，將該路徑下的 bin 資料夾加入系統 PATH。                 │
  │                       │ PATH              │                                                                                    │
  │ UNABLE_TO_GET_ISSUER_ │ 防火牆或代理伺服器  │ 執行 export NODE_USE_SYSTEM_CA=1 使用系統憑證。                                    │
  │ CERT                  │ 攔截 SSL           │                                                                                    │
  │ EACCES: permission    │ npm 安裝權限不足   │ 使用 sudo npm install -g ... 或設定 npm 免 sudo 安裝                               │
  │ denied                │                    │ (https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packag │
  │                       │                    │ es-globally)。                                                                     │
  │ Invalid API Key       │ 金鑰輸入錯誤或過期 │ 重新從 Google AI Studio 複製金鑰並更新環境變數。                                   │
  │ Request contains an   │ Google Cloud       │ 若有設定 GOOGLE_CLOUD_PROJECT 變數，嘗試將其取消設定 (unset                        │
  │ invalid argument      │ 專案衝突           │ GOOGLE_CLOUD_PROJECT)。                                                            │
  └───────────────────────┴────────────────────┴────────────────────────────────────────────────────────────────────────────────────┘

這是一份為期一週的 **Python 快速上手學習計畫**。這個計畫適合完全沒有經驗的初學者，目標是在 7 天內掌握 Python 的基礎語法，並能寫出簡單的邏輯程式。

---

# 🐍 Python 七日快速學習計畫

## 📅 學習目標
- **第一階段 (Day 1-3)**：掌握基礎語法與資料結構。
- **第二階段 (Day 4-5)**：理解程式邏輯控制與函式模組化。
- **第三階段 (Day 6-7)**：實作小專案與綜合複習。

---

## 📚 每日學習大綱

### Day 1: 環境搭建與基礎輸出
- [ ] **學習重點**：
    - 安裝 Python 與編輯器 (推薦 VS Code)。
    - 了解 `print()` 函式。
    - 變數定義與基本資料類型 (Integer, Float, String, Boolean)。
- **範例說明**：
    ```python
    # 定義變數
    name = "Alice"      # 字串 (String)
    age = 25           # 整數 (Integer)
    height = 165.5     # 浮點數 (Float)
    is_student = True   # 布林值 (Boolean)

    print(f"你好 {name}, 你今年 {age} 歲。")
    ```

### Day 2: 資料結構 (容器)
- [ ] **學習重點**：
    - 列表 (List)：儲存有序資料 $\rightarrow$ `append()`, `pop()`。
    - 字典 (Dictionary)：鍵值對儲存 $\rightarrow$ `key: value`。
    - 集合 (Set) 與 元組 (Tuple) 的簡單區別。
- **範例說明**：
    ```python
    # List 範例
    fruits = ["蘋果", "香蕉"]
    fruits.append("橘子") # 加入元素

    # Dictionary 範例
    user_info = {"name": "小明", "score": 90}
    print(user_info["name"]) # 輸出: 小明
    ```

### Day 3: 流程控制 (條件判斷)
- [ ] **學習重點**：
    - 比較運算子 (`==`, `!=`, `>`, `<`)。
    - `if`, `elif`, `else` 條件分支。
    - 邏輯運算子 (`and`, `or`, `not`)。
- **範例說明**：
    ```python
    score = 85
    if score >= 90:
        print("優秀")
    elif score >= 60:
        print("及格")
    else:
        print("不及格")
    ```

### Day 4: 迴圈控制 (Loop)
- [ ] **學習重點**：
    - `for` 迴圈：遍歷列表或範圍 (`range`)。
    - `while` 迴圈：只要條件成立就執行。
    - `break` 與 `continue` 的用法。
- **範例說明**：
    ```python
    # For 迴圈印出 0-4
    for i in range(5):
        print(f"目前數字是: {i}")

    # While 迴圈範例
    count = 3
    while count > 0:
        print(f"倒數: {count}")
        count -= 1
    ```

### Day 5: 函式 (Function) 與模組
- [ ] **學習重點**：
    - 定義函式 `def` 與參數傳遞。
    - 回傳值 `return`。
    - 導入內建模組 (如 `import random`, `import math`)。
- **範例說明**：
    ```python
    import random

    def greet(person_name):
        return f"你好, {person_name}! 歡迎學習 Python。"

    # 呼叫函式
    message = greet("學習者")
    print(message)

    # 使用模組
    print(f"隨機數字: {random.randint(1, 100)}")
    ```

### Day 6: 檔案操作與異常處理
- [ ] **學習重點**：
    - 讀寫檔案 (`open`, `with open`)。
    - 錯誤捕捉 `try...except` 避免程式崩潰。
- **範例說明**：
    ```python
    try:
        with open("test.txt", "w", encoding="utf-8") as f:
            f.write("這是 Python 學習紀錄")
        print("寫入成功！")
    except Exception as e:
        print(f"發生錯誤: {e}")
    ```

### Day 7: 綜合實作專案
- [ ] **學習重點**：
    - 將前 6 天知識整合。
    - **實作建議**：寫一個「簡易計算機」或「猜數字遊戲」。
- **實作挑戰 (猜數字遊戲邏輯)**：
    1. 使用 `random` 產生 1-100 的隨機數。
    2. 使用 `while` 迴圈讓使用者輸入猜測值。
    3. 使用 `if` 判斷猜測值是太大、太小還是正確。
    4. 正確時跳出迴圈。

---

## 🛠️ 學習建議與工具
1. **不要只看，要動手寫**：每個範例請親自輸入並執行一次。
2. **善用 Google/ChatGPT**：遇到報錯（Error）時，將錯誤訊息貼上搜尋。
3. **推薦資源**：
    - [Official Python Docs](https://docs.python.org/3/) (官方文件)
    - [W3Schools Python](https://www.w3schools.com/python/) (適合快速查閱)
    - [LeetCode](https://leetcode.com/) (後續練習演算法)

## 📈 進度追蹤表

| 天數 | 主題 | 完成狀態 | 困難度 |
| :--- | :--- | :---: | :---: |
| Day 1 | 基礎輸出與變數 | [ ] | ⭐ |
| Day 2 | 資料結構 (List/Dict) | [ ] | ⭐⭐ |
| Day 3 | 條件判斷 | [ ] | ⭐ |
| Day 4 | 迴圈控制 | [ ] | ⭐⭐ |
| Day 5 | 函式與模組 | [ ] | ⭐⭐⭐ |
| Day 6 | 檔案與異常處理 | [ ] | ⭐⭐ |
| Day 7 | 綜合實作 | [ ] | ⭐⭐⭐ |

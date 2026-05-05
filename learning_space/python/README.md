## Python 學習課綱
### 學習說明
Python 的功能非常龐大，若要將其「指令」與「函式」分類，最科學的方式是將其分為：  
**內建函式 (Built-in Functions)**、**關鍵字 (Keywords/指令)**、**標準函式庫 (StandardLibrary)** 以及 **第三方套件 (Third-party Packages)**。

以下為您詳細分類說明：

---

### 一、 關鍵字 (Keywords) —— 語言的「指令」
這些是 Python 的保留字，不能用作變數名稱。它們決定了程式的**邏輯結構**。

| 分類 | 關鍵字 (部分列舉) | 說明 |
| :--- | :--- | :--- |
| **流程控制** | `if`, `elif`, `else`, `for`, `while`, `break`, `continue`, `pass` | 用於決定程式執行的路徑與迴圈。 |
| **函數與類別** | `def`, `return`, `lambda`, `class` | 用於定義函數 (Function)與類別 (Class)。 |
| **邏輯與布林** | `and`, `or`, `not`, `True`, `False`, `is` | 邏輯運算與真假值判定。 |
| **異常處理** | `try`, `except`, `finally`, `raise`, `assert` | 捕捉錯誤並處理程式崩潰。 |
| **變數與作用域** | `global`, `nonlocal`, `import`, `from`, `as` | 定義變數範圍或引入外部模組。 |
| **其他** | `with`, `yield`, `async`, `await` | 資源管理 (Context Manager) 與非同步處理。 |

---

### 二、 內建函式 (Built-in Functions) —— 隨時可用
這些函式不需要 `import` 任何東西，直接寫在程式碼裡就能用。

| 分類 | 函式名稱 | 說明 |
| :--- | :--- | :--- |
| **輸出與輸入** | `print()`, `input()` | 顯示訊息到螢幕 / 接收使用者輸入。 |
| **型別轉換** | `int()`, `float()`, `str()`, `list()`, `dict()`, `set()`, `tuple()` | 將資料轉換為整數、浮點數、字串、列表等。 |
| **數學運算** | `abs()`, `max()`, `min()`, `sum()`, `round()`, `pow()` | 絕對值、最大/最小值、加總、四捨五入、次方。 |
| **序列與迭代** | `len()`, `range()`, `enumerate()`, `zip()`, `sorted()`, `reversed()` | 獲取長度、產生範圍、索引-數值配對、排序。 |
| **系統與檢查** | `type()`, `id()`, `help()`, `dir()`, `open()` | 檢查型別、唯一編號、查看說明、開啟檔案。 |

---

### 三、 標準函式庫 (Standard Library) —— 內建但需導入
這些是 Python 安裝後就自帶的模組，但使用前必須先用 `import` 導入。

| 模組名稱 | 常用函式/類別 | 說明 |
| :--- | :--- | :--- |
| **`os` / `sys`** | `os.path.join()`, `sys.exit()` | 操作作業系統檔案路徑、系統參數。 |
| **`math`** | `math.sqrt()`, `math.sin()`, `math.pi` | 進階數學運算 (平方根、三角函數、圓周率)。 |
| **`datetime`** | `datetime.now()`, `strftime()` | 處理日期與時間。 |
| **`random`** | `random.randint()`, `random.choice()` | 產生隨機數或隨機選取元素。 |
| **`json`** | `json.loads()`, `json.dumps()` | 處理 JSON 格式資料 (字串 $\leftrightarrow$ 字典)。 |
| **`re`** | `re.search()`, `re.findall()` | 正規表達式 (Regular Expression) 字串搜尋與取代。 |

---

### 四、 第三方套件 (Third-party Packages) —— 需安裝
這些不是 Python 內建的，需要透過 `pip install` 安裝後才能使用。

| 分類 | 常用套件 | 說明 |
| :--- | :--- | :--- |
| **數據分析** | `Pandas`, `NumPy` | 處理表格資料、矩陣運算。 |
| **資料視覺化** | `Matplotlib`, `Seaborn` | 繪製折線圖、長條圖、散佈圖。 |
| **機器學習/AI** | `PyTorch`, `TensorFlow`, `Scikit-learn` | 深度學習、預測模型。 |
| **網路請求/爬蟲** | `Requests`, `BeautifulSoup`, `Scrapy` | 抓取網頁資料、發送HTTP 請求。 |
| **網頁後端** | `Django`, `Flask`, `FastAPI` | 建立網站 API 與後端伺服器。 |

---

### 總結：如何區分？

如果你在寫程式時遇到一個詞，可以用以下邏輯判斷它是什麼：

1. **它是彩色且不能被賦值嗎？** $\rightarrow$ **關鍵字 (Keyword)** $\rightarrow$例如：`if`, `while`
2. **它後面跟著 `()` 且不需要 import？** $\rightarrow$ **內建函式 (Built-in)** $\rightarrow$ 例如：`print()`
3. **它需要 `import` 才能用，且是 Python 自帶的？** $\rightarrow$ **標準庫 (Standard Library)** $\rightarrow$ 例如：`math.sqrt()`
4. **它需要 `pip install` 才能用？** $\rightarrow$ **第三方套件 (Third-party)**$\rightarrow$ 例如：`pd.DataFrame()` (Pandas)

這份進階計畫將聚焦於 **物件導向程式設計 (OOP)、進階語言特性、非同步處理以及效能優化**。

---

# 🚀 Python 進階七日挑戰計畫

## 🎯 進階學習目標
- **深度掌握**：從單純的腳本寫法轉向模組化與物件導向架構。
- **提升效能**：學習迭代器、生成器與非同步 IO 以處理大數據與高併發。
- **專業實踐**：掌握裝飾器、上下文管理器及類型標註。

---

## 📚 進階學習大綱

### Day 1: 進階函數特性 (Functional Python)
- [ ] **學習重點**：
    - 列表推導式 (List Comprehensions) 與 字典/集合推導式。
    - Lambda 匿名函數。
    - 高階函數：`map()`, `filter()`, `sorted()`。
    - 閉包 (Closures) 的概念。
- **範例說明**：
    ```python
    # 列表推導式：篩選出 1-20 之間的所有偶數並平方
    squares = [x**2 for x in range(1, 21) if x % 2 == 0]

    # 使用 Lambda 與 sorted 對複雜列表排序 (按年齡排序)
    users = [{"name": "A", "age": 30}, {"name": "B", "age": 20}]
    sorted_users = sorted(users, key=lambda x: x['age'])
    ```

### Day 2: 物件導向深度探索 (OOP Deep Dive)
- [ ] **學習重點**：
    - 類別 (Class) 與 物件 (Object) 的深層理解。
    - 繼承 (Inheritance) 與 多型 (Polymorphism)。
    - 封裝：私有變數 (`_` 與 `__`)。
    - 魔法方法 (Magic Methods/Dunder Methods) 如 `__str__`, `__repr__`, `__len__`, `__getitem__`。
- **範例說明**：
    ```python
    class Book:
        def __init__(self, title, author):
            self.title = title
            self.author = author

        def __str__(self): # 定義 print(obj) 時顯示的內容
            return f"《{self.title}》- {self.author}"

    book = Book("Python進階", "專家")
    print(book) # 觸發 __str__
    ```

### Day 3: 裝飾器與上下文管理器 (Decorators & Context Managers)
- [ ] **學習重點**：
    - 裝飾器 (`@decorator`)：如何修改函數行為而不改變原始碼。
    - 上下文管理器 (`with` 語句)：`__enter__` 與 `__exit__`。
    - `functools.wraps` 的使用。
- **範例說明**：
    ```python
    import time

    def timer(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            print(f"執行時間: {time.time() - start:.4f}s")
            return result
        return wrapper

    @timer
    def slow_function():
        time.sleep(1)

    slow_function()
    ```

### Day 4: 迭代器與生成器 (Iterators & Generators)
- [ ] **學習重點**：
    - 迭代協議 (`__iter__`, `__next__`)。
    - 生成器函式 (`yield`)：節省記憶體的關鍵。
    - 生成器表達式 (Generator Expressions)。
- **範例說明**：
    ```python
    # 使用 yield 建立一個無限序列或大數據流
    def count_up_to(max_val):
        count = 1
        while count <= max_val:
            yield count
            count += 1

    for num in count_up_to(1000000): # 不會一次佔用大量記憶體
        if num > 5: break
        print(num)
    ```

### Day 5: 並行與非同步處理 (Concurrency & Asyncio)
- [ ] **學習重點**：
    - 多執行緒 (Threading) vs 多進程 (Multiprocessing) 的區別。
    - 全域解釋器鎖 (GIL) 的影響。
    - `asyncio` 庫：`async def` 與 `await` 的非同步編程。
- **範例說明**：
    ```python
    import asyncio

    async def say_hello():
        print("Hello...")
        await asyncio.sleep(1) # 非阻塞等待
        print("...World!")

    async def main():
        await asyncio.gather(say_hello(), say_hello())

    asyncio.run(main())
    ```

### Day 6: 類型標註與程式碼品質 (Type Hinting & Quality)
- [ ] **學習重點**：
    - 類型標註 (Type Hints)：`typing` 模組 (`List`, `Optional`, `Union`, `Callable`)。
    - 錯誤處理進階：定義自定義異常 (Custom Exceptions)。
    - PEP 8 編碼規範與 `mypy` 靜態檢查。
- **範例說明**：
    ```python
    from typing import List, Optional

    def process_scores(scores: List[int], limit: Optional[int] = None) -> List[int]:
        if limit:
            return [s for s in scores if s > limit]
        return scores
    ```

### Day 7: 進階綜合實作 (Advanced Project)
- [ ] **學習重點**：
    - 綜合運用 OOP、裝飾器、非同步或生成器。
    - **實作建議**：
        - **方案 A**：建立一個「非同步網頁爬蟲」 (使用 `httpx` 或 `aiohttp`)。
        - **方案 B**：設計一個「簡單的 ORM 框架」 (使用魔法方法與類別繼承)。
        - **方案 C**：開發一個「記憶體高效的日誌分析工具」 (使用生成器處理大檔案)。

---

## 🛠️ 進階學習路徑建議

| 階段 | 核心能力 | 推薦工具/庫 |
| :--- | :--- | :--- |
| **效能優化** | 記憶體管理 $\rightarrow$ 生成器 $\rightarrow$ 非同步 | `asyncio`, `itertools` |
| **架構設計** | 類別繼承 $\rightarrow$ 組合 $\rightarrow$ 介面設計 | `abc` (Abstract Base Classes) |
| **工業標準** | 類型檢查 $\rightarrow$ 單元測試 $\rightarrow$ CI/CD | `pytest`, `mypy`, `pylint` |

## 💡 給進階學習者的建議
1. **閱讀原始碼**：嘗試閱讀知名開源庫（如 `requests` 或 `flask`）的原始碼，看看專業工程師如何設計類別。
2. **關注時間與空間複雜度**：在寫代碼時，開始思考 $O(n)$ 或 $O(\log n)$ 的差異。
3. **實踐重構**：將你第一週寫的基礎程式碼，用進階技巧（如推導式、裝飾器）重新重構一次。

Yocto（通常指 Yocto Project）是一個用來打造客製化 Linux 系統的工具集合，特別常用在嵌入式設備（像路由器、工業控制器、IoT 裝置）。

你可以把它想成：「自己組一個 Linux 發行版的工廠」，而不是直接用現成的像 Ubuntu 或 Debian。

🧠 Yocto 在做什麼？

它的核心其實是 建構系統（build system），會幫你：

從原始碼編譯整個 Linux 系統
自訂你要的：
Kernel（核心）
套件（例如 Python、SSH）
開機方式
產出可以燒錄到裝置的映像檔（image）
🧩 核心概念（很重要）

Yocto 有幾個關鍵組件：

1. BitBake（引擎）

👉 BitBake
負責實際執行 build 的工具，有點像 make 但更強大。

2. Layer（圖層）

就是「功能模組包」，例如：

meta（核心）
meta-openembedded（常用套件）
硬體廠提供的 layer（像 Raspberry Pi）

👉 不同 layer 疊在一起形成你的系統

3. Recipe（食譜）

副檔名 .bb
定義「怎麼編譯一個套件」

例如：

從哪抓原始碼
怎麼編譯
安裝哪些檔案
4. Image（最終系統）

你最後 build 出來的 Linux 映像

### 🚀 基本使用流程（入門版）
Step 1：準備環境（通常在 Linux）

建議用 Ubuntu：

sudo apt install gawk wget git diffstat unzip texinfo gcc build-essential chrpath
Step 2：下載 Yocto（Poky）

### 👉 官方參考發行：

git clone git://git.yoctoproject.org/poky
cd poky
Step 3：初始化環境
source oe-init-build-env

這會建立一個 build/ 資料夾

Step 4：開始 build
bitbake core-image-minimal

### 👉 這會產出一個最小 Linux 系統

Step 5：找輸出

在：

build/tmp/deploy/images/

會看到 .img 或 .wic 檔

### 🛠️ 常見應用場景

Yocto 很常用在：

IoT 裝置
工業電腦（IPC）
車用系統
客製化 Linux firmware
⚠️ 說實話：Yocto 不簡單

我直接講重點：

### 👉 Yocto 的學習曲線很陡

你會卡的點通常是：

layer 相依性
recipe 撰寫
build error 很難看懂
編譯時間超長（幾小時起跳）
### 🤔 Yocto 適合你嗎？

👉 適合：

你要做 embedded Linux
需要完全客製系統
有長期維護需求

👉 不適合：

只是想跑 Linux
想快速做 prototype

👉 那種情況用：

Raspberry Pi OS
Buildroot（更簡單）
📌 如果你要入門，我建議這樣走
先 build core-image-minimal
試著加入一個套件（例如 nano）
再學 layer 概念
最後才碰 recipe

#!/bin/bash

# 檢查是否有提供參數
if [ $# -eq 0 ]; then
  echo "請提供一個數字作為參數，例如：./script.sh 5"
  exit 1
fi

# 取得第一個參數
num=$1

# 計算平方
square=$((num * num))

# 顯示結果
echo "$num 的平方是 $square"
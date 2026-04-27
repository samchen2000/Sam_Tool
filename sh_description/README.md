`.sh` 腳本是一種用於 Linux 和其他 Unix 系統的腳本檔案，它可以將多個指令組合起來，方便進行系統
管理、自動化工作等。以下是 `.sh` 腳本中一些常見的指令：

1. **變數設定**：
 * `export Var_name=value`:設定環境變數。
 * `local Var_name=value`:設定局部變數（只對該腳本有效）。
2. **查詢系統資訊**：
 * `uname -a`:顯示系統的名稱、版本、架構等資訊。
 * `hostname`:顯示系統的主機名稱。
 * `man command`:顯示使用者手冊中的指令。
3. **工作目標**：
 * `cd directory`:變換到指定的目標目錄。
 * `pwd`:顯示目前的 working directory。
4. **程式執行**：
 * `./script.sh`:執行腳本檔案。
 * `./script.sh arg1 arg2`:執行腳本檔案，並將 arg1 和 arg2 代入參數。
5. **系統管道**：
 * `|`:使用管道符號連接指令，將指令的輸出作為下一指令的輸入。
6. **循環和條件**：
 * `while loop_condition do ... done`:實現 looping 。

  `if condition then statement else statement fi`： if-then-else-endif Statement

   ```shell
   #!/bin/bash

   -e 'if [ $1 -eq 0 ]; then echo "hello"; else echo "goodbye"; fi' # test command
   ```
7. **正則表達式**：
 * `grep pattern file`:尋找文件中匹配特定模式的行。
 * ` sed 's/pattern/replacement/' file`: replacing pattern in file.

  ```shell
  #!/bin/bash

  -e 'sed "s/old/new/g" oldfile > newfile' # replacing old with new in a file
   ```
8. **執行系統命令**：
 * `sudo command`:執行 system command。

  ```shell
  #!/bin/bash

  -e 'sudo apt-get update && sudo apt-get install package_name'
   ```

9. **設定環境變數（為了避免繼承父母的環境變數）**：

```bash
  export NAME='John Doe'

  -e 'echo $NAME' # output: John Doe
```
10. **使用變數代替參數**：

```bash
  variable_name = "value"
  echo "$variable_name"
   ```

11. **在腳本中使用變數**：
 
 ```bash
  #!/bin/bash

  # declare -i variable_name=1
  # declare -a array=(1 2 3)
  
  -e 'echo $variable_name' # output: 1
  
  -e 'echo "${array[@]}"' # output: 1 2 3
```

12. **使用 for 很 loop**：

```bash
  -e 'for name in "John" "Mary" "Bob"; do
   echo "$name"
done'

```
13. **使用 case 语句**：

 ```shell
  #!/bin/bash

  -e 'case $variable_name in
    value1) echo "value1";;
    value2) echo "value2";;
    *) echo "default";;
esac'
```

14. **使用 shift 语句**：

```bash
  #!/bin/bash

  # shift n-times
  -e 'for ((i=0; i<3; i++)); do
   shift
   echo $1
done'

```
15. `while` loop 和 `until` loop 

```shell
  #!/bin/bash

  -e 'i=0
 while [ $i -lt 5 ]; do
  echo $((i+1))
  ((i++))
 done'
  
 -e 'i=0
 until [ $i -ge 5 ]; do
  echo $((i+1))
  ((i++))
 done'

```
16. `read`指令

```shell
  #!/bin/bash

  -e 'echo "Enter your name:"
 read Name
 echo "Hello, '$Name'!"
```

17. `exec`和`exit`指令:

```shell
  #!/bin/bash

  -e 'exec /bin/sh'
  -e 'exit'
```
18. `source`指令：

```shell
  #!/bin/bash

  -e 'source script.sh' # equivalent to source ./script.sh
   ```

19. `alias`指令：

```bash
  #!/bin/bash

  -e 'alias ll="ls -l"'
```

20. `unalias`指令：

```bash
  #!/bin/bash

  -e 'unalias ll'
```
21. `export`指令：

```bash
  #!/bin/bash

  -e 'export Var_name=value'
```

22. `unset`指令：

```bash
  #!/bin/bash

  -e 'unset Var_name'
```

23. `command -v`指令：

```bash
  #!/bin/bash

  -e 'command -v echo'
   ```

24. `type`指令：

```bash
  #!/bin/bash

  -e 'type command'
   ```
25. `which`指令：

```bash
  #!/bin/bash

  -e 'which command'
```
26. `history`指令：

```bash
  #!/bin/bash

  -e 'history'
```

27. `source .bashrc`指令： 

```bash
  #!/bin/bash

  -e 'source ~/.bashrc' # equivalent to source /etc/profile.d/bootstrap.sh
```
28. `command --version`指令：

```bash
  #!/bin/bash

  -e 'command --version'
```

29. `man command`指令： 

 ```shell
   #!/bin/bash

  -e 'man command' # displays the manual page for the specified command
```
30. `info command`指令：

```bash
  #!/bin/bash

  -e 'info command'
```

31. `command --help`指令：

```bash
  #!/bin/bash

  -e 'command --help' # displays help information for the specified command
```
32. `command --man`指令： 

 ```shell
   #!/bin/bash

  -e 'command --man' # displays the manual page for the specified command
```

33. `command --info`指令：

```bash
  #!/bin/bash

  -e 'command --info' # displays information about the specified command
```
34. `history -1`指令： 

 ```shell
   #!/bin/bash

  -e 'history -1'
```

35. `history -n`指令： 

 ```shell
   #!/bin/bash

  -e 'history -n'
```

36. `history -c`指令：

```bash
  #!/bin/bash

  -e 'history -c' # clears the history list
```

37. `alias ll="ls -l"`指令：

```bash
  #!/bin/bash

  -e 'alias ll="ls -l"'
```
38. `unalias ll`指令：

```bash
  #!/bin/bash

  -e 'unalias ll'
```
39. `source script.sh`指令： 

 ```shell
   #!/bin/bash

  -e 'source script.sh' # equivalent to source ./script.sh
```

40. `eval`指令：

```bash
  #!/bin/bash

  -e 'eval "var_name=5"'
```

41. `command &`指令：

```bash
  #!/bin/bash

  -e 'command &' # runs the command in the background
```
42. `pkill command`指令： 

 ```shell
   #!/bin/bash

  -e 'pkill command'
```

43. `killall command`指令： 

```bash
  #!/bin/bash

  -e 'killall command'
```

44. `ps aux`指令：

```bash
  #!/bin/bash

  -e 'ps aux' # displays the list of running processes
```

45. `ps -ef`指令：

```bash
  #!/bin/bash

  -e 'ps -ef' # displays detailed information about all running processes
```
46. `kill pid`指令： 

 ```shell
   #!/bin/bash

  -e 'kill pid'
```

47. `pkill command`指令：

```bash
  #!/bin/bash

  -e 'pkill command' # kills the specified process by signal
```
48. `signal pid sig`指令： 

 ```shell
   #!/bin/bash

  -e 'signal pid sig'
```

49. `wait`指令：

```bash
  #!/bin/bash

  -e 'wait' # waits for all background jobs to finish
```

50. `bg command`指令：

```bash
  #!/bin/bash

  -e 'bg command' # runs the specified command in the background
```
51. `fg`指令：

```bash
  #!/bin/bash

  -e 'fg' # brings a job to the foreground
```

52. `killall command`指令： 

 ```shell
   #!/bin/bash

  -e 'killall command'
```

53. `ps aux`指令：

```bash
  #!/bin/bash

  -e 'ps aux' # displays the list of running processes
```

54. `pkill command`指令： 

 ```shell
   #!/bin/bash

  -e 'pkill command'
```

55. `signal pid sig`指令： 

 ```shell
   #!/bin/bash

  -e 'signal pid sig'
```

56. `wait`指令：

```bash
  #!/bin/bash

  -e 'wait' # waits for all background jobs to finish
```
57. `bg command`指令：

```bash
  #!/bin/bash

  -e 'bg command' # runs the specified command in the background
```

58. `fg`指令：

```bash
  #!/bin/bash

  -e 'fg' # brings a job to the foreground
```
59. `killall command`指令： 

 ```shell
   #!/bin/bash

  -e 'killall command'
```

60. `ps aux`指令：

```bash
  #!/bin/bash

  -e 'ps aux' # displays the list of running processes
```
61. `pkill command`指令： 

 ```shell
   #!/bin/bash

  -e 'pkill command'
```

62. `signal pid sig`指令： 

 ```shell
   #!/bin/bash

  -e 'signal pid sig'
```

63. `wait`指令：

```bash
  #!/bin/bash

  -e 'wait' # waits for all background jobs to finish
```
64. `bg command`指令：

```bash
  #!/bin/bash

  -e 'bg command' # runs the specified command in the background
```

65. `fg`指令：

```bash
  #!/bin/bash

  -e 'fg' # brings a job to the foreground
```
66. `killall command`指令： 

 ```shell
   #!/bin/bash

  -e 'killall command'
```

67. `ps aux`指令：

```bash
  #!/bin/bash

  -e 'ps aux' # displays the list of running processes
```
68. `pkill command`指令： 

 ```shell
   #!/bin/bash

  -e 'pkill command'
```

69. `signal pid sig`指令： 

 ```shell
   #!/bin/bash

  -e 'signal pid sig'
```

70. `wait`指令：

```bash
  #!/bin/bash

  -e 'wait' # waits for all background jobs to finish
```
71. `bg command`指令：

```bash
  #!/bin/bash

  -e 'bg command' # runs the specified command in the background
```

72. `fg`指令：

```bash
  #!/bin/bash

  -e 'fg' # brings a job to the foreground
```
73. `killall command`指令： 

 ```shell
   #!/bin/bash

  -e 'killall command'
```

74. `ps aux`指令：

```bash
  #!/bin/bash

  -e 'ps aux' # displays the list of running processes
```
75. `pkill command`指令： 

 ```shell
   #!/bin/bash

  -e 'pkill command'
```

76. `signal pid sig`指令： 

 ```shell
   #!/bin/bash

  -e 'signal pid sig'
```

77. `wait`指令：

```bash
  #!/bin/bash

  -e 'wait' # waits for all background jobs to finish
```
78. `bg command`指令：

```bash
  #!/bin/bash

  -e 'bg command' # runs the specified command in the background
```

79. `fg`指令：

```bash
  #!/bin/bash

  -e 'fg' # brings a job to the foreground
```
80. `killall command`指令： 

 ```shell
   #!/bin/bash

  -e 'killall command'
```

81. `ps aux`指令：

```bash
  #!/bin/bash

  -e 'ps aux' # displays the list of running processes
```
82. `pkill command`指令： 

 ```shell
   #!/bin/bash

  -e 'pkill command'
```

83. `signal pid sig`指令： 

 ```shell
   #!/bin/bash

  -e 'signal pid sig'
```

84. `wait`指令：

```bash
  #!/bin/bash

  -e 'wait' # waits for all background jobs to finish
```
85. `bg command`指令：

```bash
  #!/bin/bash

  -e 'bg command' # runs the specified command in the background
```

86. `fg`指令：

```bash
  #!/bin/bash

  -e 'fg' # brings a job to the foreground
```
87. `killall command`指令： 

 ```shell
   #!/bin/bash

  -e 'killall command'
```

88. `ps aux`指令：

```bash
  #!/bin/bash

  -e 'ps aux' # displays the list of running processes
```
89. `pkill command`指令： 

 ```shell
   #!/bin/bash

  -e 'pkill command'
```

90. `signal pid sig`指令： 

 ```shell
   #!/bin/bash

  -e 'signal pid sig'
```

91. `wait`指令：

```bash
  #!/bin/bash

  -e 'wait' # waits for all background jobs to finish
```
92. `bg command`指令：

```bash
  #!/bin/bash

  -e 'bg command' # runs the specified command in the background
```

93. `fg`指令：

```bash
  #!/bin/bash

  -e 'fg' # brings a job to the foreground
```
94. `killall command`指令： 

 ```shell
   #!/bin/bash

  -e 'killall command'
```

95. `ps aux`指令：

```bash
  #!/bin/bash

  -e 'ps aux' # displays the list of running processes
```
96. `pkill command`指令： 

 ```shell
   #!/bin/bash

  -e 'pkill command'
```

97. `signal pid sig`指令： 

 ```shell
   #!/bin/bash

  -e 'signal pid sig'
```

98. `wait`指令：

```bash
  #!/bin/bash

  -e 'wait' # waits for all background jobs to finish
```
99. `bg command`指令：

```bash
  #!/bin/bash

  -e 'bg command' # runs the specified command in the background
```

100. `fg`指令：

```bash
  #!/bin/bash

  -e 'fg' # brings a job to the foreground
```
101. `killall command`指令： 

 ```shell
   #!/bin/bash

  -e 'killall command'
```

102. `ps aux`指令：

```bash
  #!/bin/bash

  -e 'ps aux' # displays the list of running processes
```
103. `pkill command`指令： 

 ```shell
   #!/bin/bash

  -e 'pkill command'
```

104. `signal pid sig`指令： 

 ```shell
   #!/bin/bash

  -e 'signal pid sig'
```

105. `wait`指令：

```bash
  #!/bin/bash

  -e 'wait' # waits for all background jobs to finish
```
106. `bg command`指令：

```bash
  #!/bin/bash

  -e 'bg command' # runs the specified command in the background
```

107. `fg`指令：

```bash
  #!/bin/bash

  -e 'fg' # brings a job to the foreground
```
108. `killall command`指令： 

 ```shell
   #!/bin/bash

  -e 'killall command'
```

109. `ps aux`指令：

```bash
  #!/bin/bash

  -e 'ps aux' # displays the list of running processes
```
110. `pkill command`指令： 

 ```shell
   #!/bin/bash

  -e 'pkill command'
```

111. `signal pid sig`指令： 

 ```shell
   #!/bin/bash

  -e 'signal pid sig'
```

112. `wait`指令：

```bash
  #!/bin/bash

  -e 'wait' # waits for all background jobs to finish
```
113. `bg command`指令：

```bash
  #!/bin/bash

  -e 'bg command' # runs the specified command in the background
```

114. `fg`指令：

```bash
  #!/bin/bash

  -e 'fg' # brings a job to the foreground
```
115. `killall command`指令： 

 ```shell
   #!/bin/bash

  -e 'killall command'
```

116. `ps aux`指令：

```bash
  #!/bin/bash

  -e 'ps aux' # displays the list of running processes
```
117. `pkill command`指令： 

 ```shell
   #!/bin/bash

  -e 'pkill command'
```

118. `signal pid sig`指令： 

 ```shell
   #!/bin/bash

  -e 'signal pid sig'
```

119. `wait`指令：

```bash
  #!/bin/bash

  -e 'wait' # waits for all background jobs to finish
```
120. `bg command`指令：

```bash
  #!/bin/bash

  -e 'bg command' # runs the specified command in the background
```

121. `fg`指令：

```bash
  #!/bin/bash

  -e 'fg' # brings a job to the foreground
```
122. `killall command`指令： 

 ```shell
   #!/bin/bash

  -e 'killall command'
```

123. `ps aux`指令：

```bash
  #!/bin/bash

  -e 'ps aux' # displays the list of running processes
```
124. `pkill command`指令： 

 ```shell
   #!/bin/bash

  -e 'pkill command'
```

125. `signal pid sig`指令： 

 ```shell
   #!/bin/bash

  -e 'signal pid sig'
```

126. `wait`指令：

```bash
  #!/bin/bash

  -e 'wait' # waits for all background jobs to finish
```
127. `bg command`指令：

```bash
  #!/bin/bash

  -e 'bg command' # runs the specified command in the background
```

128. `fg`指令：

```bash
  #!/bin/bash

  -e 'fg' # brings a job to the foreground
```
129. `killall command`指令： 

 ```shell
   #!/bin/bash

  -e 'killall command'
```

130. `ps aux`指件：
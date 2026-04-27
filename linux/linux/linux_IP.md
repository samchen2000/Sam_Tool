## 設定IP位址的過程取決於操作系統和網路環境。 一般來說，設定IP位址包含獲取IP位址、子網路遮罩和預設閘道，可以透過DHCP自動分配，也可以手動設定。

### 1. 使用ifconfig命令(較舊的系統):
- 打開終端機。
- 輸入 sudo ifconfig "interface" "ip_address" netmask "<netmask>" up 來設定IP位址和子網路遮罩，其中<interface>是網路介面名稱，例如eth0或wlan0。
- 輸入 sudo route add default gw <gateway_ip_address> <interface> 來設定預設閘道。
- 設定IP : ifconfig (interface) (ip_address) netmask (gateway_ip_address) 
### 2. 使用ip命令(較新的系統):
- 打開終端機。
- 輸入 sudo ip addr add <ip_address>/<prefix_length> dev <interface> 來設定IP位址和子網路遮罩。
- 輸入 sudo ip route add default via <gateway_ip_address> 來設定預設閘道。
- 可以通過ip link set <interface> up來啟用網路介面。

### 注意事項:
- 請確保輸入的IP位址、子網路遮罩和閘道位址在您的網路環境中是有效的。
- 在手動設定IP位址之前，最好先記錄下目前的設定，以便日後恢復。
- 某些網路環境可能需要設定DNS伺服器。


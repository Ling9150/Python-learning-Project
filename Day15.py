for i_1 in range(1,5,3):
    print(i_1)
print()
for i_2 in range(6,0,-1):
    print(i_2)
word = "Ping"
for char in word:
    print(char)
for i_3 in range(254,249,-1):
    print(f"172.16.99.{i_3}\n"+"-"*30)
    if i_3 == 254:
        print("核心主网关")
    elif i_3 == 253:
        print("备用网关")
    else:
        print("未知网络设备")
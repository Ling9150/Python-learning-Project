for i in range(1,11):
    print(i)
    ip = f"192.168.100.{i}"
    print(ip)
    if i== 1:
        print("发现网关设备")
    elif i == 8:
        print("发现核心服务器")
    else:
        print("普通终端机")
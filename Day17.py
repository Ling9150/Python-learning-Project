while True:
    ip_address = input("请输入IP地址（q键退出）")
    ip_clean = ip_address.strip()
    print(ip_clean)
    #简单写法 if ip_clean.lower() == "q":
    if ip_clean == "q":
        print("下班")
        break
    elif ip_clean == "Q":
        print("下班")
        break
    else:
        number = ip_clean.split(".")
        last_number = number[-1]
        if last_number == "254":
            print("网关设备")
        elif last_number == "1":
            print("核心交换机")
        else:
            print("普通主机")



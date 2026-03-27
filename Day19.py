switches = ["10.0.0.1","10.0.0.2"]
print(f"早上机房有{switches}")
switches.append("10.0.0.3")
print(f"新设备上架后：{switches}")
switches.remove("10.0.0.1")
print(f"坏设备下线后：{switches}")
print()
ips = ["192.168.1.10","192.163.1.11","192.168.1.12"]
for ip in ips:
    print(f"正在SSH登录设备：{ip}")
    print("下发全局配置：ntp server 1.1.1.1")
    print("配置保存成功 \n")
print("所有设备配置下发完毕")
ips_list = ["10.1.1.10","10.1.1.20","10.1.1.30"]
ips_list.append("10.1.1.88")
ips_list.remove("10.1.1.20")
print(f"割接后的最新列表为{ips_list}")
for ip_check in ips_list:
    print("开始巡检设备")
    if ip_check == "10.1.1.88":
        print("注意，新上架，需检查")
    else:
        print("老设备正常运行")
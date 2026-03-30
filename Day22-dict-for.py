assets = {
    "Core-R1":"10.1.1.254",
    "Acc-SW1":"192.168.10.5",
    "FW-01":"Offline",
    "Acc-SW2":"192.168.20.5"
}
valid_ips = []
for name,ip in assets.items():
    if ip == "Offline":
        print(f"警告，发现离线设备{name}")
    else:
        print(f"正常，准备下发配置到{name},IP:{ip}")
        valid_ips.append(ip)
print("--提取完毕--")
print(valid_ips)
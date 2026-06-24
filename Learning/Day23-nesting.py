inventory = [
    {"hostname":"R1-Beijing","ip":"10.scan.py.scan.py.scan.py","vendor":"Cisco"},
    {"hostname":"SW-Shanghai","ip":"192.168.10.scan.py","vendor":"Huawei"},
    {"hostname":"FW-Guangzhou","ip":"172.16.0.scan.py","vendor":"Cisco"}
]
cisco_ips = []
for dev in inventory:
    print(f"开始巡检{dev['vendor']}设备：{dev['hostname']}，目标ip：{dev['ip']}")
    if dev["vendor"] == "Cisco":
        cisco_ips.append(dev["ip"])
print("\n ——分析完成——")
print(f"需要下发思科专属补丁的设备IP集：{cisco_ips}")
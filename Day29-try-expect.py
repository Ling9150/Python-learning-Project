try:
    with open("nobody.txt","r") as f:
        cotent = f.readline()
except:
    print("文件找不到")
cloud_devices = [
    {"ip": "10.0.0.1", "model": "Cisco 9300"},
    {"ip": "10.0.0.2"},  # 🚨 致命缺陷：缺少 model 键！
    {"ip": "10.0.0.3", "model": "Huawei S5700"},
    {"model": "H3C S6520"}  # 🚨 致命缺陷：缺少 ip 键！
]
def print_device_info(device_list):
    for line in device_list:
        try:
            ip = line["ip"]
            model = line["model"]
            print(f"设备ip是{ip}，型号是{model}")
        except:
            print("发现残缺数据，已跳过")
print_device_info(cloud_devices)
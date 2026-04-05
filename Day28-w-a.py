with open("report.txt","w",encoding="utf-8") as f:
    f.write("===核心交换机配置===") #不会自动换行
    f.write("IP:192.168.1.1\n")
with open("report.txt","a",encoding="utf-8") as f:
    f.write("2023-10-25")
network_devices = [
    {"ip": "192.168.1.1", "name": "Core-SW01", "status": "Up"},
    {"ip": "192.168.1.2", "name": "Acc-SW02", "status": "Down"},
    {"ip": "10.0.0.254", "name": "FW-01", "status": "Up"},
    {"ip": "172.16.1.5", "name": "Server-01", "status": "Down"}
]
def generate_reports(device_list):
    with open("urgent_alerts.txt","w",encoding="utf-8")as fi:
        fi.write("===最新宕机设备===\n")
    for device in device_list:
        current_ip = device["ip"]
        current_name = device["name"]
        current_status = device["status"]
        with open("all_log.txt","a",encoding="utf-8") as file:
            file.write(f"{current_ip},{current_name},{current_status},\n")
        if current_status.lower() == "down":
            with open("urgent_alerts.txt","a",encoding="utf-8") as fi:
                fi.write(f"{current_name}的ip是{current_ip},\n")
generate_reports(network_devices)
import json
# 云端返回的复杂 JSON 字符串
api_response = '''
{
    "device_id": "FW-Core-9981",
    "uptime_seconds": 86400,
    "network_data": {
        "mac_address": "AA:BB:CC:DD:EE:FF",
        "interfaces": [
            {
                "name": "ge0/0",
                "role": "LAN",
                "status": "Active",
                "details": {"ip": "192.168.1.254", "gateway": null}
            },
            {
                "name": "ge0/1",
                "role": "WAN",
                "status": "Down",
                "details": {"ip": "100.64.1.2", "gateway": "100.64.1.1"}
            },
            {
                "name": "ge0/2",
                "role": "WAN",
                "status": "Active",
                "details": {"ip": "203.0.113.5", "gateway": "203.0.113.1"}
            }
        ]
    }
}
'''
active_wan = []
python_data = json.loads(api_response)
for data in python_data["network_data"]["interfaces"]:
            if data["status"] == "Active":
                print("检测到一个活跃")
                if data["role"] == "WAN":
                    active_wan.append(data["name"])
                    active_wan.append(data["details"]["ip"])
                    active_wan.append(data["details"]["gateway"])
                    # 以后可以这样塞数据：
                    #active_wan.append({
                    #    "name": data["name"],
                    #    "ip": data["details"]["ip"],
                    #    "gateway": data["details"]["gateway"]
                    #})
                    name = data["name"]
                    ip = data["details"]["ip"]
                    gateway = data["details"]["gateway"]
print(active_wan)
print(f"当前活动公网接口为{name},ip:{ip},网关:{gateway}") #错误！这个要放到for循环里面，要“发现一个，打印一个”

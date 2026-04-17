import json
import yaml
#模拟数据
raw_api_response = """
{
    "requestId": "ALI-889900",
    "data": {
        "total_count": 3,
        "instances": [
            {"instance_id": "server-A", "status": "Running", "network": {"public_ip": "8.8.8.8", "bandwidth": 10}},
            {"instance_id": "server-B", "status": "Stopped", "network": {"public_ip": "1.1.1.1", "bandwidth": 5}},
            {"instance_id": "server-C", "status": "Running", "network": {"public_ip": "2.2.2.2", "bandwidth": 100}}
        ]
    }
}
"""
py_res = json.loads(raw_api_response)
line = []
for data in py_res["data"]["instances"]:
    sta = data["status"]
    bw = int(data["network"]["bandwidth"])
    id = data["instance_id"]
    p_ip = data["network"]["public_ip"]
    print(sta)
    if "running" in sta.lower() and bw>= 10:
        box = {}
        box["id"] = id
        box["ip"] = p_ip
        line.append(box)
print(line)
ya_d = yaml.safe_dump(line)
with open("vip_servers.yaml","w",encoding="utf-8")as f:
    f.write(ya_d)



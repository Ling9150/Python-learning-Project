import json
aws_api_response = '''
{
    "region": "ap-northeast-1",
    "servers": [
        {"name": "Web-01", "ip": "47.1.1.1", "status": "running"},
        {"name": "DB-01", "ip": "47.1.1.2", "status": "stopped"},
        {"name": "Web-02", "ip": "47.1.1.3", "status": "running"}
    ]
}
'''
print(type(aws_api_response))
def extract_running_ips(api_data):
    try:
        python_dict = json.loads(api_data)
    except:
        print("数据解析失败")
        return
    running_ip = []
    for line in python_dict["servers"]:
        if line["status"] == "running":
            running_ip.append(line["ip"])
            print(running_ip)
    with open("running_ips.txt","a",encoding="utf-8")as file:
        for ip in running_ip:
            file.write(f"正在运行的有：{ip}\n")
extract_running_ips(aws_api_response)

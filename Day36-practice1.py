import requests
res = requests.get("https://jsonplaceholder.typicode.com/users")
print(res.status_code)
assets_list = res.json()
print(assets_list)
print("——抓取结果——")
for asset in assets_list:
    device_name = asset["name"]
    device_ip = asset["phone"]
    print(f"设备名:{device_name},管理ip:{device_ip}")
with open("audit_assets.txt","w",encoding="utf-8")as file:
    for tar in assets_list:
        if tar["email"][-4:] == ".biz":
            print("发现目标设备")
            n = tar["name"]
            e = tar["email"]
            print(n,e)
            file.write(n)
            file.write(e)
            #file.write(f"设备名:{n}  邮箱:{e}\n")

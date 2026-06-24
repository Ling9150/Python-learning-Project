import requests
import json

ip_ad = input("请输入需要追踪的恶意ip地址：")
pac = requests.get(f"http://ip-api.com/json/{ip_ad}?lang=zh-CN")
print(pac.status_code)
if pac.status_code == 200:
    r = pac.json()
    print(r)
    con = r["country"]
    city = r["city"]
    print(f"恶意地址所在国家为{con},城市是{city}")
else:
    print("网络请求失败")
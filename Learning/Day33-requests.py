import requests
import json
package = requests.get("https://api.ipify.org?format=json")
print(package.status_code)
#改进做法：if package.status_code == 200
json_data = package.text
data = json.loads(json_data) #解析功能已有，可以直接这样写：data = package.json()
print(f"获取到{data}") #改进做法：data["ip"]
'''res = requests.get("https://books.toscrape.com/")
if res.ok:
    print(res.text)
else:
    print("失败")'''
head = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"
}
r = requests.get("https://movie.douban.com/top250",headers=head)
print(r.status_code)

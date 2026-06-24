import requests
import json
package = requests.get("https://api.ipify.org?format=json")
print(package.status_code)
#改进做法：if package.status_code == 200
json_data = package.text
data = json.loads(json_data) #解析功能已有，可以直接这样写：data = package.json()
print(f"获取到{data}") #改进做法：data["ip"]
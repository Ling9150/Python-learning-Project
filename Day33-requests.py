import requests
import json
package = requests.get("https://api.ipify.org?format=json")
print(package.status_code)
json_data = package.text
data = json.loads(json_data)
print(f"获取到{data}")
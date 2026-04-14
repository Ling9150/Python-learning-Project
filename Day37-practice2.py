import requests
try:  #以后写脚本，try 里面尽量只包住那些“真的会因为外部原因崩溃”的代码，如果是网络问题，它会提示网络错误；如果是你后续写的代码或字段名敲错了，Python 会给你报出具体的红字错误，方便定位。
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    py_res = response.json()
    print(f"——发现符合条件的设备——")
    for data in py_res:
        name = data["name"]
        lat = data["address"]["geo"]["lat"]
        r_name = data["company"]["name"]
        if float(lat) > 0:
            print(f"设备名称：{name},维度：{lat},归属租户：{r_name}")
except:
    print("请求失败")

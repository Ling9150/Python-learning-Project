import requests
r = requests.get("https://jsonplaceholder.typicode.com/users")
p_r = r.json()
#print(p_r)
final_data = {
    "monitoring_targets":[]
}
#data = {
#    "coordinates":{}
#}  Python里的箱子，不是物理纸箱，它更像是一个共享文档.Python非常偷懒！它并没有把文档里的字复印一份放进最终列表，它只是把“链接A”这个网址塞进了列表里！
for d in p_r:
    name = d["name"]
    com = d["company"]["name"]
    lat = d["address"]["geo"]["lat"]
    lng = d["address"]["geo"]["lng"]
    if float(lat) > 0:
        data = {
            "coordinates": {}
        }
        #每遇到一个符合条件的，就新建一个空白的、拥有全新链接的文档
        data["server_name"] = name
        data["tenant"] = com
        data["coordinates"]["lat"] = float(lat)
        data["coordinates"]["lng"] = float(lng)
        final_data["monitoring_targets"].append(data)
print(final_data)

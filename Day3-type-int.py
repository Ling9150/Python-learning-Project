vlan_id = input("输入VLAN号：")
print(type(vlan_id))
a = 10
print(type(a))
num_id = int(vlan_id)
total = num_id + a
print(total)
total1 = int(input("总端口数："))
con = int(input("已插线数："))
print("剩余可用",total1-con)

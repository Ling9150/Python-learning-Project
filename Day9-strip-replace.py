dirty_ip = "  192.168.1.203   \n   0/0/1 \n"
print(dirty_ip)
clean_ip = dirty_ip.strip()  #不能去除中间的空格和换行
print(clean_ip)
interface = "GigabitEthernet0/0/3"
short_interface = interface.replace("GigabitEthernet","GE")
print(short_interface)
print(interface.replace("/"," "))
model = "  Huawei Ar6666   "
print(model.strip())
win_mac = "00-E0-FC-11-22-33"
print(win_mac.replace("-",""))
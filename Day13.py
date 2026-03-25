raw_ip = "  172.16.88.254 \n"
clean_ip = raw_ip.strip()
ip_blocks = clean_ip.split(".")
print(ip_blocks)
last_number = ip_blocks[-1]
if last_number == "254":
    print("网关地址")
elif last_number =="0":
    print("网络号，不可分配")
elif last_number =="255":
    print("广播地址")
else:
    print("普通主机地址")
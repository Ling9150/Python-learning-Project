port_status = "DOWN"
if port_status == "UP":
    print("运行正常")
else:
    print("宕掉了，请检查")
target_ip = "192.168.1.254"
if target_ip == "192.168.1.254":
    print("这是网关地址")
else:
    print("这是普通主机地址")
bgp_status = "Established \n"
new_status = bgp_status.strip()
if new_status == "Established":
    print("BGP邻居建立成功")
else:
    print("BGP邻居未建立")
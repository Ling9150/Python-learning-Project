core_switches = ["10.0.0.1","10.0.0.2"]
print(f"主核心交换机IP是{core_switches[0]}")
ips = ["192.168.1.254","10.1.1.1","10.1.1.2","10.1.1.3","172.16.0.88"]
print(f"本网络的网关IP是{ips[0]}")
last_ip = ips[-1]
print(f"测试主机的IP是{last_ip}")
agg_switches = ips[1:4]
print("汇聚层设备列表为",agg_switches)
name = "C"
ip = "10.0.2.1"
port = 5
message = "交换机"+name+"的ip是"+ip+",故障端口是"+str(port)
print(message)
message1 = f"交换机{name}的ip是{ip}，故障端口是{port}"
print(message1)
total_ports = 48
used_ports = 15
print(f"交换机还剩下{total_ports-used_ports}")
print(f"ip是{ip}的交换机已经被使用，除此之外还有{used_ports-1}个正在使用的交换机")
dest_ip = input("目标网段是：")
mask = input("子网掩码是：")
next_hop = input("下一跳ip：")
print(f"ip route-static {dest_ip} {mask} {next_hop}")
net = "192.128.2."
host = 257
full_ip = net+str(host)
print(full_ip)
port_1 = int(input("请输入正在配置的端口号："))
next_port = port_1+1
prefix = "GigabitEthernet0/0/"
print(prefix+str(next_port))

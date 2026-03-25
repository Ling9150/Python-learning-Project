vlan_id = 20
cpu_usage = 15.5
print(vlan_id)
print(cpu_usage)
total_ports = 48
used_ports = 12
free_ports = total_ports-used_ports
print(free_ports)
total_ips = 256 #总ip数
reserved_ips = 2
gateway = 1
dhcp_pool = 100
static_ips = total_ips-reserved_ips-gateway-dhcp_pool
print("静态可用ip数量为",static_ips)
num1 = 5
num2 = 2.5
print(num1/num2)
print(num1+num2)
print(num1*num2)
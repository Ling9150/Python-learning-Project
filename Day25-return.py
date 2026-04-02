def m_c(ip):
    config = f"interface vlan1\n ip address {ip} 255.255.255.0"
    return config
my_file_content = m_c("192.168.1.1")
print(my_file_content)
interfaces = {
    "Gi0/1":1,
    "Gi0/2":2,
    "Gi0/3":3,
    "Gi0/4":4
}
def get_port_status(code):
    if code == 1:
        return "UP"
    elif code == 2:
        return "Down"
    elif code == 3:
        return "Admin Down"
    else:
        return "Unknown"
for name,code in interfaces.items():
    real_status = get_port_status(code)
    print(f"接口{name}的当前状态是：{real_status}")
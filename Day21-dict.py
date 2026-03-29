core_switch = {
    "hostname":"Core-SW-01",
    "ip":"10.0.0.254"
}
print(core_switch)
core_switch["username"] = "admin"
print(f"增加后{core_switch}")
firewall = {
    "name":"FW-Edge-01",
    "ip":"192.168.100.1",
    "vendor":"Cisco"
}
name = firewall["name"]
ip = firewall["ip"]
print(f"正在配置设备{name}，管理ip为{ip}。")
firewall["port"] = "8443"
firewall["ip"] = "10.255.255.1"
print(firewall)

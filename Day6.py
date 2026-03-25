banner = """=====
警告，您已登录核心交换机！
=====
"""
print(banner)
port_name = "Gigabit0/0/1"
vlan_id = 10
desc = "To_HR_PC"
config_block = f"""
 interface{port_name}
 description{desc}
 vlan id{vlan_id}"""
print(config_block)
port1 = input("接口名称：")
allow_vlan = input("VLAN列表：")
cf = f'''interface {port1}
 description Uplink_Port
 port link_type trunk
 port trunk allow-pass vlan {allow_vlan}'''
print(cf)
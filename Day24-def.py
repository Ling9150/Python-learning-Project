def cf(i_name,v_id):
    print(f"interface {i_name}")
    print(f" switchport mode access")
    print(f" switchport access vlan {v_id}")
    print(f" no shudown")
cf("GigabitEthernet0/1",10)
def create_vlan(vlan_id,vlan_name):
    print(f"vlan {vlan_id}")
    print(f" name {vlan_name}")
    print(" state active")
    print("!")
vlans_to_add = [
    {"id":"VLAN 10","name":"IT_Dept"},
    {"id":"VLAN 20","name":"Finance"},
    {"id":"VLAN 30","name":"Guest"}
]
for dev in vlans_to_add:
    create_vlan(dev["id"],dev["name"])
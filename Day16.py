for port in range(1,25):
    print(f"interface GigabitEthernet0/{port}")
    if port != 24:
        print(" switchport mode access")
        print(" switchport access vlan 100")
        print("!")
    else:
        print("switchport mode trunk")
        print("switchport trunk allowed vlan all")
        print("!")

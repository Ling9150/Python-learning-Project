#\d{min,max}
#\.转义
import re
arp_log = """
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.1.1.254             -    c401.1234.abcd  ARPA   Vlan1
Internet  192.168.100.scan.py         12    a1b2.c3d4.e5f6  ARPA   Vlan2
"""
res = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",arp_log)
print(res)
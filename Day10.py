ip = "192. 168. 1. 259 \n"
octets1 = ip.split(".")
octets2 = ip.split() #换行也能切
octets3 = ip.split(". ")
print(octets1)
print(octets2)
print(octets3)
print(octets3[1])
print(octets3[1:])
network = "172.16.100.0/24"
print(network.split(".")[0])
arp_line = "192.168.1.10 00e0-fc11-2233 ARPA Vlanif10"
print(arp_line.split()[-3])

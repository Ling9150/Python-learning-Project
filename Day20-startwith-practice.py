all_ips = ["192.168.1.1","10.1.1.2","192.168.1.3","172.16.0.1"]
lan_ips = []
for ip in all_ips:
    if ip.startswith("192"):
        lan_ips.append(ip)
print(f"筛选出来的网段为{lan_ips}")
log_ips = ["192.168.1.254","10.255.0.1","172.16.0.88","10.0.0.5","8.8.8.8","10.1.1.254"]
mgmt_ips = []
for ips in log_ips:
    if ips.startswith("10."):   #要加“."，不然100也会被匹配到
        mgmt_ips.append(ips)
print(f"从日志中提取到的管理网IP有：{mgmt_ips}")
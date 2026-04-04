with open("targets.txt","r",encoding="utf-8") as file:
    valid_ips = []
    for line in file.readlines(): #readline只读文件第一行
        clean_ip = line.strip()
        valid_ips.append(clean_ip)
print(valid_ips)
for ips in valid_ips:
    print(f"【执行】正在向目标{ips}发送Ping包…")
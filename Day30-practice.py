with open("raw_ips.txt","w",encoding="utf-8")as file:
    file.write("""192.168.1.10
10.0.0.5  

Error: Connection refused
  172.16.0.254  

   Timeout
192.168.1.11""")
try:
    with open("raw_ips.txt","r",encoding="utf-8")as f:
        f.readlines()
except FileExistsError:
    print("找不到原始文件，请检查")

def clean_ip_data(content):
    cleandata = []
    with open(content,"r",encoding="utf-8")as fi:
        for line in fi.readlines():
            data = line.strip()
            print(data)
            if data == "":
                continue
            elif "error" in data.lower() or "timeout" in data.lower():
                print("错误")
            else:
                print("干净ip")
                cleandata.append(data)
        print(cleandata)
    for ip in cleandata:
        with open("clean_ips.txt", "a", encoding="utf-8") as f1:
            f1.write(f"{ip}\n")
    #此种写法更好
    #with open("clean_ips.txt", "w", encoding="utf-8") as f1:
        #for ip in cleandata:
            #f1.write(f"{ip}\n")
clean_ip_data("raw_ips.txt")

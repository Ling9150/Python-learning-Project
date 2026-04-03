def get_cidr_format(ip,mask):
    mask_map = {
        "255.255.255.0":"24",
        "255.255.255.128":"25",
        "255.255.255.252":"30",
        "255.255.255.255":32
    }
    num = mask_map[mask]
    ip_mask = f"{ip}/{num}"
    return ip_mask
ip_mask1 = get_cidr_format("10.10.10.5","255.255.255.252")
ip_mask2 = get_cidr_format("172.16.0.1","255.255.255.128")
print(f"转换成功！标准网络格式为：{ip_mask1}")
print(f"转换成功，标准网络格式为{ip_mask2}")
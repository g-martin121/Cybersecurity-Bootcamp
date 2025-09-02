def filter_ips(ip_list):
    return sorted(list(set(ip_list)))

ip = ["192.168.1.1", "10.0.0.1", "192.168.1.1"]
print(filter_ips(ip))


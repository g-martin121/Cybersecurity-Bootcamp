import re
log = "Error from 192.168.1.1"
ip = re.search(r"\d+\.\d+\.\d+\.\d+", log)

if ip:
    print(ip.group())
else:
    print("IP not found.")




import socket
log_entry = [("bing.com", 80), ("bing.com", 443)]
host = "bing.com"
ports = [80, 443]

for port in ports:
    s = socket.socket()
    s.settimeout(1)
    result = s.connect_ex((host, port))
    
    if result == 0:
        print(f"Port {port} is OPEN.")
    else:
        print(f"Port {port} is CLOSED.")
    
    s.close()

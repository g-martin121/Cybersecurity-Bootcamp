import psutil
from datetime import datetime
import time

def monitor_connections():
    try:
        for i in range(3):
            timestamp = datetime.now().strftime("%Y%m%d %H:%M:%S")
            print(f"\nCurrent time: {timestamp}")
            connections = psutil.net_connections(kind="tcp")

            for conn in connections:
                print(f" IP: {conn.laddr.ip} Port: {conn.laddr.port}")
            time.sleep(10)

    except PermissionError:
        print("Permission denied")
    except psutil.AccessDenied:
        print("Access denied.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    monitor_connections()
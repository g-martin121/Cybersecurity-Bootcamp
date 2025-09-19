import psutil
from datetime import datetime
import time

def monitor_connections():
    try:
        for i in range(3):
            timestamp = datetime.now().strftime("%m%d%Y %H:%M:%S")
            print(f"\nScan {i+1} at {timestamp} (Layer 4: transport)")

            for conn in psutil.net_connections(kind="tcp"):
                if conn.status == "ESTABLISHED":
                    local = f"{conn.laddr.ip}: {conn.laddr.port}"
                    remote = f"{conn.raddr.ip}: {conn.raddr.port}" if conn.raddr else "None"
                    print(f"Local: {local}, Remote: {remote}")

            time.sleep(10)
            
    except psutil.AccessDenied:
        print("Access denied.")
    except PermissionError:
        print("Run as administrator.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    monitor_connections()
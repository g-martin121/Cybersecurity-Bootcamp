import platform
import socket
import shutil

print("\n--- System Information ---\n")

computer_name = socket.gethostname()
print(f"Computer Name: {computer_name}")

operating_system = platform.system()
os_version = platform.release()
print(f"Operating System: {operating_system} {os_version}")

disk = shutil.disk_usage("/")
free_space_gb = disk.free / (1024 ** 3)  # Convert bytes to GB
print(f"AvailableDisk Space: {free_space_gb:.2f} GB\n")

if __name__ == "__main__":
    print("System information retrieved successfully.\n")
import os

try:
    print("=== running services ===")
    os.system("sc query state= all")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
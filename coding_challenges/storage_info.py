import shutil

def storage_info(path):
    try:
        total, used, free = shutil.disk_usage(path)
        print(f"Total: {total // (2**30)} GB")
        print(f"Used: {used // (2**30)} GB")
        print(f"Free: {free // (2**30)} GB")
    except Exception as e:
        print(f"Error retrieving storage info: {e}")

if __name__ == "__main__":
    storage_info("/")  # Change "/" to the desired path if needed
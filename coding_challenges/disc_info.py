import subprocess

def disk_info():
    try:
        result = subprocess.run(["diskutil", "list"], capture_output=True, text=True)
        return result.stdout
    
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        return None

if __name__ == "__main__":
    info = disk_info()
    print(info)
import subprocess

def system_profiler():
    try:
        result = subprocess.run(["system_profiler", "SPHardwareDataType"], capture_output=True, text=True)

        return result.stdout
    
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        return None

if __name__ == "__main__":
    info = system_profiler()
    print(info)

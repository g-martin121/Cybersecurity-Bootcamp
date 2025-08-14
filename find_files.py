import os

folder = "/home/kali"
extension = ".txt"  

try:
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(extension):
                print(os.path.join(root, file))
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("File search completed without errors.")

if __name__ == "__main__":
    folder = "/home/kali"
    extension = ".txt"
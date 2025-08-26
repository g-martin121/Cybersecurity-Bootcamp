import os

def list_files(path):
    try:
        items = os.listdir(path)
        print(f"Files in {path}:")
        for item in items:
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                size = os.path.getsize(item_path)
                print(f"{item}:{size} bytes")
    except FileNotFoundError:
        print(f"The file {path} was not found.")
    except PermissionError:
        print(f"Permission to read {path} was denied.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    list_files(r"C:\Users\marti")
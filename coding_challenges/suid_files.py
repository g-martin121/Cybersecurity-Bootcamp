import os
import stat

def list_suid_file(path):
    try:
        items = os.listdir(path)
        print(f" SUID Files in {path}:")
        for item in items:
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                st_mode = os.stat(item_path).st_mode
                permissions = stat.filemode(os.stat(item_path).st_mode)
            if st_mode & stat.S_ISUID:
                print(f"{item}: {permissions}")

    except FileNotFoundError:
        print(f"{path} does not exist")
    except PermissionError:
        print(f" You don't have permission to this {path}")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    list_suid_file("/usr/bin")
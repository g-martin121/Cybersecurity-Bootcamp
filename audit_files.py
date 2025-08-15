import os
import stat


def audit_writable(path):
    try:
        print(f"World-writable files in {path}:")
        for root, _, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    if os.stat(file_path).st_mode & stat.S_IWOTH:
                        print(file_path)
                except PermissionError:
                    print(f"Error: Permission denied for {path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    audit_writable("/tmp")
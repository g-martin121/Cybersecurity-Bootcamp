import winreg

def get_os_info():
    try:
        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Microsoft\Windows NT\CurrentVersion",
            0,
            winreg.KEY_READ
        )

        product_name = winreg.QueryValueEx(key, "ProductName")[0]
        current_version = winreg.QueryValueEx(key, "CurrentVersion")[0]

        return f"OS: {product_name}, Version: {current_version}"

    except PermissionError:
        return "Error: Permission denied"
    except FileNotFoundError:
        return "Error: Registry key or value not found"
    except Exception as e:
        return f"Unexpected error: {e}"

if __name__ == "__main__":
    print(get_os_info())

def list_users():
    passwd_path = "/etc/passwd"
    try:
        with open(passwd_path, "r") as f:
            print("Usernames found:\n")
            for line in f:
                if line.strip() and ":" in line:
                    username = line.split(":")[0]
                    print(username)
    except FileNotFoundError:
        print(f"The file {passwd_path} was not found.")
    except PermissionError:
        print(f"Permission to read {passwd_path} was denied.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    list_users()
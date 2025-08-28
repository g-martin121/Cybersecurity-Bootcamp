def list_group_members():
    path = "/etc/group"
    try:
        with open(path, "r") as f:
            print("Group members:")
            for line in f:
                if line.strip() and ":" in line:
                    members = line.split(":")[0]
                    print(members)
    except FileNotFoundError:
        print(f"The file {path} was not found.")
    except PermissionError:
        print(f"Permission to read {path} was denied.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    list_group_members()
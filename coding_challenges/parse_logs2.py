import csv

def parse_logs2(file_path):
    try:
        with open(file_path, "r") as f:
            reader = csv.DictReader(f)
            print("Failed login events (ID 4625):")
            for row in reader:
                if row.get("EventID") == "4625":
                    time = row.get("TimeCreated")
                    user = row.get("AccountName", "Unknown")
                    print(f"Time: {time}, User: {user}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parse_logs2(r"C:\Users\marti\Documents\security_log2.csv")
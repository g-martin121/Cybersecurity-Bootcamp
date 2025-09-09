import csv

def parse_logs(filename):
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            print("Failed login attempts (Event ID 4625):\n")
            for row in reader:
                if row.get("EventID") == "4625":
                    time = row.get("TimeCreated") or row.get("Date")
                    user = row.get("Account Name") or row.get("User")
                    print("Time: {time}, User: {user}")
    except FileNotFoundError:
        print("Error: File '(filename)' not found.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    parse_logs(r"C:\Users\marti\Documents\security_log.csv")
#import operating system
import os

def list_directories(path):
    try:
        #items is everything listed in the path you choose
        items = os.listdir(path)
        print (f"Directories in {path}:")
        for item in items:
            #take every path and item if its a folder and print it
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                print(item)
    except FileNotFoundError:
        print(f"Directory '{path}' not found")
    except PermissionError:
        print(f"Permission denied for '{path}'")
    except Exception as e:
        print(f"Error occurred: {e}")
        
if __name__ == "__main__":
    list_directories("/home")
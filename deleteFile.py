import shutil
import os

path = 'test.txt'

try: 
    os.remove(path) # does not delete directories (folders) 
    # os.rmdir(path) to remove empty directories
    # shutil.rmtree(path) to remove directories and everything in them, super dangerous
except FileNotFoundError:
    print("File Not Found")
except PermissionError:
    print("You are not allowed to delete that!")
except OSError:
    print("You cannot delete that with that function!")
else: 
    print(path + " was deleted")
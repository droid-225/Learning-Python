import os

source = "test.txt"
destination = "new_location\\moved.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination) # can also be used to move directories
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found")
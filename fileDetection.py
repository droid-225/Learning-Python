import os

path = "test.txt"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file!")
    elif os.path.isdir(path): # checks if given path points to a directory or folder
        print("That is a directory!")
else:
    print("That location doesn't exist!")
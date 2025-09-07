try:
    with open('test.txt') as f: # automatically closes files once read, but does not catch or handle exceptions
        print(f.read())
except FileNotFoundError as e:
    print("File Not Found!")

#print(f.closed) # only works if file is found
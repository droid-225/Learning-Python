import time

myTime = int(input("Enter the time in seconds: "))

for x in range(myTime, 0, -1): # negative step also allows us to count backwards
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    # print statement automatically adds a newline character at end of each line
    # to change the end character, use print(output, end = " ") to add a space at the end of the line
    # the end variable can be any string including "", " ", "-", etc.
    time.sleep(1)

#time.sleep(3) # sleeps for given amount of seconds

print("Time's UP!")
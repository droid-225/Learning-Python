import time

myTime = int(input("Enter the time in seconds: "))

for x in range(myTime, 0, -1): # negative step also allows us to count backwards
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

#time.sleep(3) # sleeps for given amount of seconds

print("Time's UP!")
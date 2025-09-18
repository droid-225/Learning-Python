# daemon thread : a thread that runs in the background, not important to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed, stay alive until task is complete
#                 ex. background tasks, garbage collection, waiting for input, long running processes

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for: ", count, "seconds")

x = threading.Thread(target=timer, daemon=True) # automatically kills thread once main program ends
# setDaemon() can also be used to make a thread a daemon and vice-versa
# isDaemon() returns weather a thread is a daemon or not
x.start()

answer = input("Do you wish to exit?")
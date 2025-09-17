# thread : a flow of execution. Like a separate order of instructions.
#          However, each thread takes a turn running to achieve concurrency
#          GIL (global interpreter lock) only allows one thread to hold control
#          of the Python interpreter at any one time

# cpu bound : program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound : program/task spends most of it's time waiting for external events (user input, web scraping)
#            use multithreading

import threading
import time

def eat_breaky():
    time.sleep(3) # task will take 3 seconds
    print("You ate breakfast!")

def dink_cofefe():
    time.sleep(4)
    print("You drank coffee!")

def stuuudy():
    time.sleep(5)
    print("You studied!")

x = threading.Thread(target=eat_breaky, args=())
x.start()
y = threading.Thread(target=dink_cofefe, args=())
y.start()
z = threading.Thread(target=stuuudy, args=())
z.start()

#x.join() # forces main thread to wait for thread x to finish before executing
#y.join()
#z.join()

#eat_breaky()
#dink_cofefe()
#stuuudy()

print(threading.active_count()) # prints how many threads are currently running
print(threading.enumerate()) # prints a list of the threads running
print(time.perf_counter()) # prints the time it took to perform the thread
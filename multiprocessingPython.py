# multiprocessing : running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   better for cpu tasks (heavy cpu usage)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0

    while count < num:
        count += 1

def main():
    init_time = time.perf_counter()
    print(cpu_count())
    a = Process(target=counter, args=(125000000, )) # arguments must be passed as a tuple (same for multithreading)
    a.start()

    b = Process(target=counter, args=(125000000, ))
    b.start()

    c = Process(target=counter, args=(125000000, ))
    c.start()

    d = Process(target=counter, args=(125000000, ))
    d.start()

    e = Process(target=counter, args=(125000000, ))
    e.start()

    f = Process(target=counter, args=(125000000, ))
    f.start()

    g = Process(target=counter, args=(125000000, ))
    g.start()

    h = Process(target=counter, args=(125000000, ))
    h.start()

    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()

    # there is significant overhead when staring and ending a process

    print("finished in: ", time.perf_counter() - init_time, "seconds")

if __name__ == '__main__':
    main()
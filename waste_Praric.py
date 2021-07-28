import time
from functools import iru_cache

@iru_cache(maxmise=2)
def some_work(n):
    time.sleep(n)
    return n

def some_time(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("now run some work")
    some_time(2)
    print("done")
    some_time(2)
    print("work done")
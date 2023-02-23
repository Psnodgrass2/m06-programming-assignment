import random
import multiprocessing
from datetime import datetime
import time

def printrandnum():
    print("I started now " + str(datetime.now()))
    timedelay = random.random()
    time.sleep(timedelay)
    print("I ended now " + str(datetime.now()))
    return
iterator = 0
if __name__ == '__main__':
    while iterator != 3:
        iterator += 1
        p = multiprocessing.Process(target=printrandnum)
        p.start()
import time
from threading import Thread, Event
import random
import sys


def sleepMe(stop_event, task):
    n = random.randint(0, 60)
    time.sleep(n)
    print("Ответ через {} секунд, поток № {}".format(n, task))
    stop_event.clear()


def thread_gen(tasks):
    for task in tasks:
        thread = Thread(target=sleepMe, args=(STOP_EVENT, task, ))
        yield thread


def thread_start(threads):
    for thread in threads:
        thread.daemon = True
        thread.start()
        # print(thread)


STOP_EVENT = Event()
STOP_EVENT.set()
TASKS = ["{}".format(i) for i in range(20)]
THREADS = list(thread_gen(TASKS))

thread_start(THREADS)


while True:
    if not STOP_EVENT.is_set():
        print('stop_event worked')
        sys.exit()






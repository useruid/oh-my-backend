import time
import threading
from threading import Thread


def sleepMe(i):
    print("Поток {} засыпает на {} секунд.\n".format(i, i))
    time.sleep(i)
    print("""Поток {}: {} сейчас проснулся. \n
          Активных потоков: {}.\n""".format(
        i,
        threading.current_thread(),
        threading.active_count()
    )
         )


for i in range(10):
    th = Thread(target=sleepMe, args=(i, ))
    th.start()
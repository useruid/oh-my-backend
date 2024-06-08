import threading

for thread in threading.enumerate():
    print("Имя потока: {}".format(thread.getName()))
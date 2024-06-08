import threading


def delayed():
    print("Вывод через 5 секунд!")


thread = threading.Timer(5, delayed)
thread.start()
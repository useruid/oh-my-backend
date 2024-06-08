import time


def read_big_file():
    time.sleep(2)


def func_1():
    print("start func 1")
    start = time.time()
    read_big_file()
    print(f"func 1: {time.time() - start} seconds")


def func_2():
    print("start func 2")
    start = time.time()
    read_big_file()
    print(f"func 2: {time.time() - start} seconds")


def func_3():
    print("start func 3")
    start = time.time()
    read_big_file()
    print(f"func 3: {time.time() - start} seconds")


def sync_main():
    start = time.time()
    func_1()
    func_2()
    func_3()
    print(f"all time: {time.time() - start} seconds")


if __name__ == '__main__':
    sync_main()

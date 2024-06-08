import time
import multiprocessing


def dummy_func(secs):    
    print(f'Я буду делать что-то ооочень сложное целых {secs} секунд...')
    time.sleep(secs)
    print(f'Я сделяль! За {secs} секунд.')
    return f'Я сделяль! За {secs} секунд.'


if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        sleep_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 1, 1, 1]
        res = pool.map(dummy_func, sleep_times)
        print(res)
        print("That's all for now")
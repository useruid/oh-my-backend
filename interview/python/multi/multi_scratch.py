import time
import multiprocessing


def dummy_func(secs, return_list):    
    print(f'Я буду делать что-то ооочень сложное целых {secs} секунд...')
    time.sleep(secs)
    return_list.append(f'Я сделяль! За {secs} секунд.')
    

if __name__ == '__main__':

    manager = multiprocessing.Manager()
    return_list = manager.list()

    p1 = multiprocessing.Process(target=dummy_func, args=(10, return_list))
    p2 = multiprocessing.Process(target=dummy_func, args=(12, return_list))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(return_list)
    print("That's all for now")


import time

def dummy_func(secs):    
    print(f'Я буду делать что-то ооочень сложное целых {secs} секунд...')
    time.sleep(secs)
    print(f'Я сделяль! За {secs} секунд.')

dummy_func(5)
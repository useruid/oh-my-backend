from time import sleep


def counter():
    value = 0
    while True:
        print(value)
        value += 1
        yield


def printer():
    value = 0
    while True:
        if value % 3 == 0:
            print('Im printer and I wanna print')
        value += 1
        yield


def main(q: list):
    while True:
        task = q.pop(0)
        next(task)
        q.append(task)
        sleep(0.5)


if __name__ == '__main__':
    queue = []

    cnt = counter()
    queue.append(cnt)

    prt = printer()
    queue.append(prt)

    main(queue)


import asyncio

from asyncio import Task, Future
from asyncio.coroutines import coroutine

async def test():
    print('start sleeping')
    await asyncio.sleep(3)


tsk = test()



loop.run_until_complete(test())
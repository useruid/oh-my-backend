# корутина
import asyncio


async def some_func(task: str, sleep: int):
    print(f'Starting {task}')
    await asyncio.sleep(sleep)
    print(f'Finishing {task}')
    return sleep


async def main():
    a = some_func('a', 2)
    b = some_func('b', 4)
    # c = some_func('c', 6)

    task_a = asyncio.create_task(a)
    task_b = asyncio.create_task(b)
    # task_c = asyncio.create_task(c)
    # await asyncio.gather(task_a, task_b, task_c)

    a_res = await task_a
    b_res = await task_b

    sleep_c = a_res + b_res

    await some_func('c', sleep_c)

asyncio.run(main())

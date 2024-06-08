import time
import asyncio


async def read_big_file():
    await asyncio.sleep(2)


async def func_1():
    print("start func 1")
    start = time.time()
    await read_big_file()
    print(f"func 1: {time.time() - start} seconds")


async def func_2():
    print("start func 2")
    start = time.time()
    await read_big_file()
    print(f"func 2: {time.time() - start} seconds")


async def func_3():
    print("start func 3")
    start = time.time()
    await read_big_file()
    print(f"func 3: {time.time() - start} seconds")


async def async_main():
    start = time.time()
    await asyncio.gather(func_1(), func_2(), func_3())
    print(f"all time: {time.time() - start} seconds")


if __name__ == '__main__':
    asyncio.run(async_main())

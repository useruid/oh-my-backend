import time
import asyncio
import aiohttp
import requests

data = {"username": 'analytics', "password": 'PKJmm8Cvf9'}
response = requests.post("https://db-api.skillbox.pro/api/token", data=data)
access_token = response.json().get("access_token")

# TOKEN = "..."  # здесь нужен настоящий токен
TOKEN = access_token


async def request_1():
    async with aiohttp.ClientSession() as session:
        start = time.time()
        print("start request 1")
        async with session.post('https://db-api.skillbox.pro/api/v1/lms-dump/raw/',
                                headers={"Authorization": f"Bearer {TOKEN}"},
                                json={"sql": "select * from analytics.phases limit 10"}) as resp:
            text = await resp.text()
            print(len(text))
        print(f"request 1: {time.time() - start} seconds")


async def request_2():
    async with aiohttp.ClientSession() as session:
        start = time.time()
        print("start request 2")
        async with session.post('https://db-api.skillbox.pro/api/v1/lms-dump/raw/',
                                headers={"Authorization": f"Bearer {TOKEN}"},
                                json={"sql": "select * from analytics.phases limit 10"}) as resp:
            text = await resp.text()
            print(len(text))
        print(f"request 2: {time.time() - start} seconds")


async def request_3():
    async with aiohttp.ClientSession() as session:
        start = time.time()
        print("start request 3")
        async with session.post('https://db-api.skillbox.pro/api/v1/lms-dump/raw/',
                                headers={"Authorization": f"Bearer {TOKEN}"},
                                json={"sql": "select * from analytics.phases limit 10"}) as resp:
            text = await resp.text()
            print(len(text))
        print(f"request 3: {time.time() - start} seconds")


async def async_main():
    start = time.time()
    await asyncio.gather(request_1(), request_2(), request_3())
    print(f"all time: {time.time() - start} seconds")


if __name__ == '__main__':
    asyncio.run(async_main())

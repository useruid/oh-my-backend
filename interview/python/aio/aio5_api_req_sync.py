import time
import requests


data = {"username": 'analytics', "password": 'PKJmm8Cvf9'}
response = requests.post("https://db-api.skillbox.pro/api/token", data=data)
access_token = response.json().get("access_token")

# TOKEN = "..."  # здесь нужен настоящий токен
TOKEN = access_token


def request_1():
    start = time.time()
    print("start request 1")
    resp = requests.post('https://db-api.skillbox.pro/api/v1/lms-dump/raw/',
                         headers={"Authorization": f"Bearer {TOKEN}"},
                         json={"sql": "select * from analytics.phases limit 10"})
    text = resp.text
    print(len(text))
    print(f"request 1: {time.time() - start} seconds")


def request_2():
    start = time.time()
    print("start request 2")
    resp = requests.post('https://db-api.skillbox.pro/api/v1/lms-dump/raw/',
                         headers={"Authorization": f"Bearer {TOKEN}"},
                         json={"sql": "select * from analytics.phases limit 10"})
    text = resp.text
    print(len(text))
    print(f"request 2: {time.time() - start} seconds")


def request_3():
    start = time.time()
    print("start request 3")
    resp = requests.post('https://db-api.skillbox.pro/api/v1/lms-dump/raw/',
                         headers={"Authorization": f"Bearer {TOKEN}"},
                         json={"sql": "select * from analytics.phases limit 10"})
    text = resp.text
    print(len(text))
    print(f"request 3: {time.time() - start} seconds")


def sync_main():
    start = time.time()
    request_1()
    request_2()
    request_3()
    print(f"all time: {time.time() - start} seconds")


if __name__ == '__main__':
    sync_main()

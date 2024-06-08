import time
import concurrent.futures

value = [800000000, 70000000, 800000000, 70000000]


def counting(n):
    start = time.time()
    while n > 0:
        n -= 1
    return time.time() - start


def main():
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
        for number, time_taken in zip(value, executor.map(counting, value)):
            print('Start: {} Time taken: {}'.format(number, time_taken))
        print('Total time taken: {}'.format(time.time() - start))


if __name__ == '__main__':
    main()
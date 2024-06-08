from multiprocessing import Process, Queue

quit_value = -1


def put_data(data, q):
    print('creating data and putting it on the queue')
    for item in data:
        q.put(item)


def process_data(q):
    while True:
        data = q.get()
        print('data found to be processed: {}'.format(data))

        processed = data * 2
        print('processed data: {}'.format(processed))

        if data is quit_value:
            print('here is stop')
            break


if __name__ == '__main__':
    q = Queue()
    data = [5, 10, 13, -1, 6]

    p1 = Process(target=put_data, args=(data, q))
    p2 = Process(target=process_data, args=(q,))

    p1.start()
    p2.start()

    q.close()
    q.join_thread()

    p1.join()
    p2.join()
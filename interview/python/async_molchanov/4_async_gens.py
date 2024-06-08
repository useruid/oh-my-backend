import socket
from select import select

tasks = []
to_read = {}
to_write = {}

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 5000))
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()  # read
        print('Connection from', addr)
        client(client_socket)


def client(client_socket):
    while True:
        request = client_socket.recv(4096)   # read

        if not request:
            break
        else:
            response = 'Hello world\n'.encode()
            client_socket.send(response)  # write
    client_socket.close()

def event_loop():
    while any(tasks, to_read, to_write):
        while not tasks:
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))
tasks.append(server())
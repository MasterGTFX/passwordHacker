import socket
import sys

# HOST = 'localhost'
# PORT = 9090

HOST = sys.argv[1]
PORT = int(sys.argv[2])
PASSWORD = "secret"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f'[SERVER]: Server socket started at {HOST}:{PORT}')
    while True:
        conn, addr = server_socket.accept()
        print(f'[SERVER]:Got connection from {addr[0]}:{addr[1]}')
        client_password = conn.recv(1024).decode('ascii')
        if client_password != PASSWORD:
            print(f'[{addr[0]}]: wrong password -> {client_password}')
            conn.send("Wrong password!".encode('ascii'))
            conn.close()
        else:
            print(f'[{addr[0]}]: authorized with password -> {client_password}')
            conn.send("Connection Success!".encode('ascii'))
            while True:
                data = conn.recv(1024).decode('ascii')
                if not data:
                    break
                print(f'[{addr[0]}]: {data}')

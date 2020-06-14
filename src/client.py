import socket
import sys

# HOST = 'localhost'
# PORT = 9090

HOST = sys.argv[1]
PORT = int(sys.argv[2])
PASSWORD = sys.argv[3]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print(f'[CLIENT]: Connected to {HOST}:{PORT}')
    client_socket.sendall(PASSWORD.encode('ascii'))
    print(f'[CLIENT]: {PASSWORD} sent to server')
    server_response = client_socket.recv(1024).decode('ascii')
    print(f'[SERVER]: {server_response}')

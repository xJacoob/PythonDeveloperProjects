# Write your solution here
import socket
import time
import threading
from collections import defaultdict

if __name__ == "__main__":
    # Call your server handling logic here

    host = "0.0.0.0"
    port = 6379

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen()

    running = True
    storage = {}
    expiration = {}
    channels = defaultdict(set)
    lock = threading.Lock()

    def client_thread(conn, addr):
        global running

        try:
            while running:
                valid_parse = True
                parts = []
                data = conn.recv(1024)

                if not data:
                    break

                message = data.decode()
                split_message = message.split("\r\n")

                if split_message[0][0] != "*":
                    valid_parse = False

                else:
                    try:
                        array_length = int(split_message[0][1:])
                        for i in range(array_length):
                            parts.append((split_message[i+i+1][1:], split_message[i+i+2]))
                            expected_len = int(parts[i][0])
                            if expected_len != len(parts[i][1]):
                                valid_parse = False
                                break
                    except (ValueError, IndexError):
                        valid_parse = False

                if valid_parse:
                    if parts[0][1] == "PING":
                        if len(parts) == 1:
                            conn.send("+PONG\r\n".encode())
                        else:
                            conn.send("-Parsing error!\r\n".encode())
                    elif parts[0][1] == "EXIT":
                        if len(parts) == 1:
                            running = False
                            break
                        else:
                            conn.send("-Parsing error!\r\n".encode())
                    elif parts[0][1] == "ECHO":
                        if len(parts) == 2:
                            answer = f"${parts[1][0]}\r\n{parts[1][1]}\r\n".encode()
                            conn.send(answer)
                        else:
                            conn.send("-Parsing error!\r\n".encode())
                    elif parts[0][1] == "SET":
                        with lock:
                            if len(parts) == 3:
                                key = parts[1][1]
                                value = parts[2][1]
                                storage[key] = value
                                conn.send("+OK\r\n".encode())
                            if len(parts) == 5:
                                key = parts[1][1]
                                value = parts[2][1]
                                storage[key] = value
                                expire_time, set_time = int(parts[4][1]), time.time()
                                if expire_time < 0:
                                    conn.send("-Parsing error!\r\n".encode())
                                expiration[key] = (expire_time, set_time)
                                conn.send("+OK\r\n".encode())
                    elif parts[0][1] == "GET":
                        with lock:
                            if len(parts) == 2:
                                key = parts[1][1]
                                if key in storage and key not in expiration:
                                    value = storage[key]
                                    conn.send(f"${len(value)}\r\n{value}\r\n".encode())
                                elif key in storage and key in expiration:
                                    if expiration[key][0] + expiration[key][1] >= time.time():
                                        value = storage[key]
                                        conn.send(f"${len(value)}\r\n{value}\r\n".encode())
                                    else:
                                        conn.send("$-1\r\n".encode())
                                else:
                                    conn.send("$-1\r\n".encode())
                    elif parts[0][1] == "SUBSCRIBE":
                        with lock:
                            if len(parts) == 2:
                                channel_name = parts[1][1]
                                channels[channel_name].add(conn)
                                conn.send("+OK\r\n".encode())
                            else:
                                conn.send("-Parsing error!\r\n".encode())
                    elif parts[0][1] == "PUBLISH":
                        if len(parts) == 3:
                            channel = parts[1][1]
                            content = parts[2][1]
                            if channel in channels:
                                clients = channels[parts[1][1]]
                                with lock:
                                    for client in clients:
                                        try:
                                            client.send(f"*3\r\n$7\r\nmessage\r\n${len(channel)}\r\n{channel}\r\n${len(content)}\r\n{content}\r\n".encode())
                                        except Exception:
                                            continue
                        else:
                            conn.send("-Parsing error!\r\n".encode())
                    elif parts[0][1] == "DEL":
                        with lock:
                            if len(parts) == 2:
                                key = parts[1][1]
                                if key in storage:
                                    del storage[key]
                                    conn.send("+OK\r\n".encode())
                                else:
                                    conn.send("$-1\r\n".encode())
                    else:
                        conn.send("-Unknown command!\r\n".encode())
                else:
                    conn.send("-Parsing error!\r\n".encode())

        finally:
            with lock:
                for subs in channels.values():
                    subs.discard(conn)
            conn.close()

    server.settimeout(0.5)
    while running:
        try:
            conn, addr = server.accept()
            threading.Thread(target=client_thread, args=(conn, addr), daemon=True).start()
        except socket.timeout:
            continue
        except Exception:
            break
    server.close()

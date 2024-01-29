import socket
import json
import time

HOST = "127.0.0.1"
PORT = 6923

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept() # client socket, address
        with conn:
            print(f"{addr} connected")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                new_data = json.loads(data.decode('utf-8')) # decode
                client_username = new_data[0] # username
                client_message = new_data[1] # message
                
                if client_message:
                    conn.sendall(json.dumps([client_username, client_message, time.time()]).encode('utf-8'))
                
                
            
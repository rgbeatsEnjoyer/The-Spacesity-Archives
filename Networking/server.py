vimport socket
import json
import sys
import time

HOST = "127.0.0.1" 
if len(sys.argv) > 1:
    PORT = int(sys.argv[1])
else:
    PORT = 6969

messages = [["username","message"]]
message_num = 1
clients_pointer = {}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                valid = True
                data = conn.recv(1024)
                if not data:
                    break

                new_data = json.loads(data.decode())
                client_username = new_data[0]
                client_message = new_data[1]

                if client_username not in clients_pointer:
                    clients_pointer[client_username] = message_num
                    print(client_username, " joined (pointer:", message_num, ")")

                if client_message != "/update":
                    messages.append([client_username, client_message, time.time()])
                    message_num += 1
                    print(new_data)

                messages_slice = messages[clients_pointer[client_username]:message_num]
                conn.sendall(json.dumps(messages_slice).encode("utf-8"))
                print("Sent update to:", client_username, "pointer:", clients_pointer[client_username], "num:", len(messages_slice))
                clients_pointer[client_username] = message_num

                if client_message == "/update":
                    clients_pointer[client_username] = message_num
                
                

                
                

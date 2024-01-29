import socket
import json
import datetime
from datetime import datetime

# server
HOST = "127.0.0.1"
PORT = 6969

# arrays
commands = ["/update", "/exit", "/get_username"]

# input
username = str(input("Enter your username:"))

# iteration
while True:
    message = str(input("Enter a message:"))
    ###
    if message == commands[1]:
        break
    elif message == commands[2]:
        print(f"Your username: {username}")
    elif message:
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.connect((HOST, PORT))
            jstring = json.dumps([username, message])
            server.sendall(jstring.encode('utf-8'))
            data = server.recv(1024)
            pdata = json.loads(data)
            if message == commands[0]:
                for i in range(len(pdata)):
                    print("\n")
                    print(datetime.utcfromtimestamp(pdata[i][2] + 3600).strftime('%d-%m-%Y %H:%M'))
                    print(pdata[i][0])
                    print(pdata[i][1])
                    print("\n")
            for i in range(len(pdata)):
                print("\n")
                print(datetime.utcfromtimestamp(pdata[i][2] + 3600).strftime('%d-%m-%Y %H:%M'))
                print(pdata[i][0])
                print(pdata[i][1])
                print("\n")
        except Exception:
            print("Error, could not connect to server")
        finally:
            server.close()

    else:
        print("Please enter a valid message")

# exit
print(f"Goodbye, {username}!")
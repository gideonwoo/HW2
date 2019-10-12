import socket
import sys

HOST = sys.argv[1]  # The server's hostname or IP address
PORT = int(sys.argv[2])  # The port used by the server
filename = sys.argv[3] #filename HelloWorld.html

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(('GET /' + filename).encode())
    data = s.recv(4096)
    print(data)

print('Received', repr(data))

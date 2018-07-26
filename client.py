import socket

HOST, PORT = 'localhost', 8080

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_host, client_port = client_socket.getsockname()[:2]
print(client_host)
print(client_port)
client_socket.sendall(b'test')
data = client_socket.recv(1024)
print(data.decode())

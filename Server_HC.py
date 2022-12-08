import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 8000))
server.listen()
(client_socket, client_address) = server.accept()

filename = 'received_file_HC.jpg'
f = open(filename, "wb")
l = client_socket.recv(2048)

while l:
    f.write(l)
    l = client_socket.recv(2048)

f.close()
client_socket.close()
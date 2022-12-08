import socket

hostname = '129.114.110.97'
port = 8000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(1000)
client.connect((hostname, port))

f = open('space_image.png', 'rb')
l = f.read(2048)

while l:
    client.send(l)
    l = f.read(2048)

f.close()
client.close()

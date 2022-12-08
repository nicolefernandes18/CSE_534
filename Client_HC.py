import socket
import HuffmanCoding

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((socket.gethostname(), 1256))
# server.listen()
# client_socket, client_address = server.accept()
#
# filename = 'image.jpg'
# f = open(filename, "wb")
# l = client_socket.recv(2048)
#
# while l:
#     f.write(l)
#     l = client_socket.recv(2048)
#
# f.close()
# client_socket.close()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('', 8000))

image = HuffmanCoding.Image()
image.huffmanCode("image.jpg", "./compressed.bin", "image_compressed.jpg", toCheck=1)

f = open('image_compressed.jpg', 'rb')
l = f.read(2048)

while l:
    client.send(l)
    l = f.read(2048)

f.close()
client.close()

import pickle
import socket
import numpy as np
import cv2
import RunLengthEncoding
from numpysocket import NumpySocket
from PIL import Image, ImageOps

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 1256))
server.listen()
client_socket, client_address = server.accept()

filename = 'image.jpg'
f = open(filename, "wb")
l = client_socket.recv(2048)

while l:
    f.write(l)
    l = client_socket.recv(2048)

f.close()
client_socket.close()


fpath = "image.jpg"
img = cv2.imread(fpath, 0)
shape = img.shape
print(shape)
encoded = RunLengthEncoding.RLE_encoding(img, bits=8, binary=False)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 1234))
shape = pickle.dumps(shape)
client.send(shape)
client.close()

with NumpySocket() as s:
    s.connect((socket.gethostname(), 1234))
    s.sendall(encoded)

s.close()


import pickle
import socket
import numpy as np
from numpysocket import NumpySocket
import RunLengthEncoding
from PIL import Image, ImageOps

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 1234))
server.listen()
client_socket, client_address = server.accept()
shape = client_socket.recv(2048)
shape = pickle.loads(shape)
print(shape)
client_socket.close()
server.close()


with NumpySocket() as s:
    s.bind((socket.gethostname(), 1234))
    s.listen()
    client, client_address = s.accept()
    with client:
        encoded = client.recv()

decoded = RunLengthEncoding.RLE_decode(encoded, shape)
img = Image.fromarray(np.uint8(decoded))
img.save('received_RLE.jpg')
s.close()
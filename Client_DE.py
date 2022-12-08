import socket
import numpy as np
from numpysocket import NumpySocket
from PIL import Image, ImageOps

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# port = 8000
# ip = socket.gethostname()
# server.bind(('', port))
# server.listen(2)
# (client_socket, client_address) = server.accept()
#
# filename = 'image.png'
# f = open(filename, "wb")
# l = client_socket.recv(2048)
#
# while l:
#     f.write(l)
#     l = client_socket.recv(2048)
#
# f.close()
# client_socket.close()

img = Image.open('image.png')
img_ar = np.array(img)
original_img = np.array(img)
img_ar = np.insert(original_img, 0, 0, axis=2)
encoded = np.diff(img_ar, axis=2)
print(encoded)
hostname = socket.gethostname()
port = 8001
with NumpySocket() as s:
    s.connect((hostname, port))
    s.sendall(encoded)
print(encoded)
s.close()


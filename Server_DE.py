import socket
import numpy as np
from numpysocket import NumpySocket
from PIL import Image, ImageOps

hostname = socket.gethostname()
port = 8001

with NumpySocket() as s:
    s.bind(('', port))
    s.listen(2)
    (client_socket, client_address) = s.accept()
    with client_socket:
        encoded = client_socket.recv()

decoded = np.cumsum(encoded, axis=2)
print(decoded)
img = Image.fromarray(np.uint8(decoded))
img.save('received_file_DE.png')
img.show()

client_socket.close()
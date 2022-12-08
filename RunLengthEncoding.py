import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys
import os
from PIL import Image, ImageOps


def RLE_encoding(img, bits=8, binary=True, view=True):
    """
    img: Grayscale img.
    bits: what will be the maximum run length? 2^bits
    """
    if binary:
        ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


    encoded = []
    count = 0
    prev = None
    fimg = img.flatten()
    th = 127
    for pixel in fimg:
        if binary:
            if pixel < th:
                pixel = 0
            else:
                pixel = 1
        if prev == None:
            prev = pixel
            count += 1
        else:
            if prev != pixel:
                encoded.append((count, prev))
                prev = pixel
                count = 1
            else:
                if count < (2 ** bits) - 1:
                    count += 1
                else:
                    encoded.append((count, prev))
                    prev = pixel
                    count = 1
    encoded.append((count, prev))
    print(np.array(encoded))

    return np.array(encoded)

def RLE_decode(encoded, shape):
    decoded = []
    print(encoded)
    for rl in encoded:
        r, p = rl[0], rl[1]
        decoded.extend([p] * r)
    dimg = np.array(decoded).reshape(shape)
    return dimg


# fpath = "space_image.png"
# img = cv2.imread(fpath, 0)
# shape = img.shape
# print(shape)
# encoded = RLE_encoding(img, bits=8, binary=False)
# earr = np.array(encoded)
# img = Image.fromarray(np.uint8(RLE_decode(earr, shape)))
# img.save('received_RLE.png')




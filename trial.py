import socket
import cv2
import numpy as np
from math import log10, sqrt
from PIL import Image, ImageOps
# img = Image.open('space_image.png')
# original_img = np.array(img)
# img_ar = np.insert(original_img, 0, 0, axis=2)
# encoded = np.diff(img_ar, axis=2)
# decoded = np.cumsum(encoded, axis=2)
# print((original_img==decoded))
# img = Image.fromarray(np.uint8(decoded))
# img.save('my.png')
# img.show()
#
def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if (mse == 0):  # MSE is zero means no noise is present in the signal .
        # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr


def main():
    original = cv2.imread('space_image.png')
    compressed = cv2.imread('received_file_DE.png', 1)
    value = PSNR(original, compressed)
    print(f"PSNR value is {value} dB")


if __name__ == "__main__":
    main()





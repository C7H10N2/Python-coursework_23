import numpy as np 
from PIL import Image

class Imgprocess(object):
    def __init__(self, img):
        self.img = img

    def pixel(self, x, y):
        return self.img[x, y]
    
    def rgb2gray(self):
        gray = 0.3 * self.img[:, :, 0] + 0.59 * self.img[:, :, 1] + 0.11 * self.img[:, :, 2]
        gray = gray.astype(np.uint8)
        return gray

    def save(self, name):
        gray = self.rgb2gray()
        gray = Image.fromarray(gray)
        gray.save(name)

if __name__ == '__main__':
    img = Image.open('./lab5/lena.png')
    img = np.array(img)
    img = Imgprocess(img)
    print('1. Pixel of [5,6] is: '+str(img.pixel(5, 6)))
    img.save('./lab5/lena_gray.png')
    print('2. Gray image saved in: ./lab5/lena_gray.png')

# Lab5

## PIL库的应用
```python
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
```

## 程序解释

本次实验要求编写一个图像处理的Python脚本，使用PIL（Python Imaging Library）包。代码定义了一个名为`Imgprocess`的类，其中包含了对图像进行处理的方法。以下是对每个方法的解释：

`__init__`方法：初始化方法，用于创建一个`Imgprocess`对象，并将图像传递给对象。

`pixel`方法：该方法用于返回指定坐标的像素值。

`rgb2gray`方法：该方法将彩色图像转换为灰度图像。这里的转换采用以下公式：灰度值 = 0.3 * R + 0.59 * G + 0.11 * B。该方法返回一个灰度图像。

`save`方法：该方法将灰度图像保存到指定文件名的文件中。

在`main`函数中，使用PIL库打开一张彩色图像，并将其转换为一个numpy数组。然后将该数组传递给`Imgprocess`对象，并调用`pixel`方法获取指定像素点的值。接下来，将图像转换为灰度图像并使用`save`方法保存到指定文件名的文件中。最后，程序输出了两行文字，分别是像素点的值和保存灰度图像的文件路径。

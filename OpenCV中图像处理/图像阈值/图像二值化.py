"""
图像二值化：
定义：图像的二值化，就是将图像上的像素点的灰度值设置为0或255，
也就是将整个图像呈现出明显的只有黑和白的视觉效果。
灰度值0：黑  灰度值255：白
一幅图像包括目标物体、背景还有噪声，要想从多值的数字图像中直接提取出目标物体，
常用的方法就是设定一个阈值T，用T将图像的数据分成两部分：
大于T的像素群和小于T的像素群。
这是研究灰度变换的最特殊的方法，称为图像的二值化（Binarization）。

ret, dst = cv.threshold( src, thresh, maxval, type[, dst] )
参数说明：
src：原图像。
dst：结果图像。
thresh：当前阈值。
maxVal：最大阈值，一般为255.
thresholdType:阈值类型，主要有下面几种：
enum ThresholdTypes {
    THRESH_BINARY     = 0,  大于阈值的部分被置为255，小于部分被置为0
    THRESH_BINARY_INV = 1,  大于阈值部分被置为0，小于部分被置为255
    THRESH_TRUNC      = 2,  大于阈值部分被置为threshold，小于部分保持原样
    THRESH_TOZERO     = 3,  小于阈值部分被置为0，大于部分保持不变
    THRESH_TOZERO_INV = 4,  大于阈值部分被置为0，小于部分保持不变
    THRESH_MASK       = 7,
    THRESH_OTSU       = 8,
    THRESH_TRIANGLE   = 16
};
返回值:
ret： 与参数thresh一致
dst： 结果图像
使用了THRESH_OTSU和THRESH_TRIANGLE两个标志时，输入图像必须为单通道。
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread(r'C:\Users\admin\Desktop\test_picture\maomao.jpg', 0)
ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
ret1, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
ret2, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
ret3, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
ret4, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

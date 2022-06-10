"""
自适应阈值
在上一节中，我们使用一个全局值作为阈值。但这可能并非在所有情况下都很好，例如，如果图像在不同区域具有不同的光照条件。
在这种情况下，自适应阈值阈值化可以提供帮助。在此，算法基于像素周围的小区域确定像素的阈值。
因此，对于同一图像的不同区域，我们获得了不同的阈值，这为光照度变化的图像提供了更好的结果。
adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C, dst=None):
除上述参数外，方法**cv.adaptiveThreshold**还包含三个输入参数：
该**adaptiveMethod**决定阈值是如何计算的：
cv.ADAPTIVE_THRESH_MEAN_C::阈值是邻近区域的平均值减去常数**C**。
cv.ADAPTIVE_THRESH_GAUSSIAN_C:阈值是邻域值的高斯加权总和减去常数**C**。
该**BLOCKSIZE**确定附近区域的大小，**C**是从邻域像素的平均或加权总和中减去的一个常数。
下面的代码比较了光照变化的图像的全局阈值和自适应阈值：
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread(r'C:\Users\admin\Desktop\test_picture\maomao.jpg', 0)
img = cv.medianBlur(img, 5)
ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
'''
adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C, dst=None):
src：灰度化的图片
maxValue：满足条件的像素点需要设置的灰度值
adaptiveMethod：自适应方法。有2种：ADAPTIVE_THRESH_MEAN_C 或 ADAPTIVE_THRESH_GAUSSIAN_C
thresholdType：二值化方法，可以设置为THRESH_BINARY或者THRESH_BINARY_INV
blockSize：分割计算的区域大小，取奇数
C：常数，每个区域计算出的阈值的基础上在减去这个常数作为这个区域的最终阈值，可以为负数
dst：输出图像，可选
'''
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                           cv.THRESH_BINARY, 11, 3)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                           cv.THRESH_BINARY, 11, 3)
titles1 = ['Original Image', 'Global Thresholding (v = 127)',
           'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles1[i])
    plt.xticks([]), plt.yticks([])
plt.show()

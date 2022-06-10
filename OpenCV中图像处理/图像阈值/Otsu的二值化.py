"""
目标
在本教程中，您将学习简单阈值，自适应阈值和Otsu阈值。
你将学习函数**cv.threshold**和**cv.adaptiveThreshold**。
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

'''
Otsu的二值化
在全局阈值化中，我们使用任意选择的值作为阈值。相反，Otsu的方法避免了必须选择一个值并自动确定它的情况。
考虑仅具有两个不同图像值的图像（双峰图像），其中直方图将仅包含两个峰。一个好的阈值应该在这两个值的中间。
类似地，Otsu的方法从图像直方图中确定最佳全局阈值。
为此，使用了**cv.threshold**作为附加标志传递。阈值可以任意选择。然后，算法找到最佳阈值，该阈值作为第一输出返回。
'''

img = cv.imread(r'C:\Users\admin\Desktop\test_picture\maomao.jpg', 0)
# 全局阈值
ret7, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# Otsu阈值
ret8, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
'''
高斯滤波：
GaussianBlur(src, ksize, sigmaX, dst=None, sigmaY=None, borderType=None):
参数
src:输入图像
ksize:(核的宽度,核的高度)，输入高斯核的尺寸，核的宽高都必须是正奇数。否则，将会从参数sigma中计算得到。
dst:输出图像，尺寸与输入图像一致。
sigmaX:高斯核在X方向上的标准差。
sigmaY:高斯核在Y方向上的标准差。默认为None，如果sigmaY=0，则它将被设置为与sigmaX相等的值。
如果这两者都为0,则它们的值会从ksize中计算得到。计算公式为：
sigma = 0.3*((ksize - 1)* 0.5 -1)+0.8
borderType:像素外推法，默认为None（参考官方文档BorderTypes)
'''
# 高斯滤波后再采用Otsu阈值
blur = cv.GaussianBlur(img, (5, 5), 0)
ret3, th3 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
# 绘制所有图像及其直方图
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)',
          'Original Noisy Image', 'Histogram', "Otsu's Thresholding",
          'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]
for i in range(3):
    plt.subplot(3, 3, i * 3 + 1), plt.imshow(images[i * 3], 'gray')
    plt.title(titles[i * 3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i * 3 + 2), plt.hist(images[i * 3].ravel(), 256)
    plt.title(titles[i * 3 + 1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i * 3 + 3), plt.imshow(images[i * 3 + 2], 'gray')
    plt.title(titles[i * 3 + 2]), plt.xticks([]), plt.yticks([])
plt.show()

"""
目标：使用各种低通滤镜模糊图像 - 将定制的滤镜应用于图像（2D卷积）
与一维信号一样，还可以使用各种低通滤波器（LPF），高通滤波器（HPF）等对图像进行滤波。
LPF有助于消除噪声，使图像模糊等。HPF滤波器有助于在图像中找到边缘。
OpenCV提供了一个函数**cv.filter2D**来将内核与图像进行卷积。例如，我们将尝试对图像进行平均滤波。5x5平均滤波器内核。
操作如下:保持这个内核在一个像素上，将所有低于这个内核的25个像素相加，取其平均值，然后用新的平均值替换中心像素。
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread(r'C:\Users\Admin\Desktop\opencv\roi.jpg')
# img = cv.cvtColor(img, cv.COLOR_BGR2RGB)    # 改变图像通道
kernel = np.ones((5, 5), np.float32) / 25   # 创建平均滤波矩阵
'''
函数名：filter2D(src, ddepth, kernel, dst=None, anchor=None, delta=None, borderType=None):
.   @param ddepth 目标图像的期望深度，参见@ref filter_depth "combination "
.   @param kernel 卷积核(或者更确切地说是相关核)，一个单通道浮点数矩阵
.   @param anchor 核的锚点，它指示内部被过滤点的相对位置内核;锚点应该位于内核内;默认值(-1，-1)意味着锚点位于内核中心。
.   @param delta 在将过滤后的像素存储到dst之前添加到它们的可选值。
.   @param borderType 像素外推方法，参见#BorderTypes。不支持#BORDER_WRAP。
'''
dst = cv.filter2D(img, -1, kernel)
# plt.subplot(121), plt.imshow(img), plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
# plt.xticks([]), plt.yticks([])
# plt.show()
cv.imshow('Original', img)
cv.imshow('Averaging', dst)
key = cv.waitKey(0)
# 任意键退出
cv.destroyAllWindows()


"""
学习： - 查找图像梯度，边缘等 - 我们将看到以下函数：cv.Sobel()，cv.Scharr()，cv.Laplacian()等
OpenCV提供三种类型的梯度滤波器或高通滤波器，即Sobel，Scharr和Laplacian。

1. Sobel 和 Scharr 算子
Sobel算子是高斯平滑加微分运算的联合运算，因此它更抗噪声。逆可以指定要采用的导数方向，垂直或水平（分别通过参数yorder和xorder）。
逆还可以通过参数ksize指定内核的大小。如果ksize = -1，则使用3x3 Scharr滤波器，比3x3 Sobel滤波器具有更好的结果。

2. Laplacian 算子
它计算了由关系
Δsrc = ∂^2src/∂x^2 + ∂^2src/∂y^2
给出的图像的拉普拉斯图,它是每一阶导数通过Sobel算子计算。如果ksize = 1,然后使用以下内核用于过滤:

kernel= [ 0 1 0
         1 −4 1
         0 1 0 ]

参考学习链接： https://blog.csdn.net/qq_36622009/article/details/102900447
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread(r'C:\Users\admin\Desktop\OpenCV\dave.jpg', 0)
'''
Laplacian(src, ddepth, dst=None, ksize=None, scale=None, delta=None, borderType=None): 
.   @param ddepth 目标映像的期望深度。
.   @param ksize Aperture size used to compute the second-derivative filters. See #getDerivKernels for
.   details. The size must be positive and odd.
.   @param scale Optional scale factor for the computed Laplacian values. By default, no scaling is
.   applied. See #getDerivKernels for details.
.   @param delta Optional delta value that is added to the results prior to storing them in dst .
.   @param borderType Pixel extrapolation method, see #BorderTypes. #BORDER_WRAP is not supported.
'''
laplacian = cv.Laplacian(img, cv.CV_64F)
'''
Sobel(src, ddepth, dx, dy, dst=None, ksize=None, scale=None, delta=None, borderType=None):
.   @param src input image.
.   @param dst output image of the same size and the same number of channels as src .
.   @param ddepth output image depth, see @ref filter_depths "combinations"; in the case of
.       8-bit input images it will result in truncated derivatives.
.   @param dx order of the derivative x.
.   @param dy order of the derivative y.
.   @param ksize size of the extended Sobel kernel; it must be 1, 3, 5, or 7.
.   @param scale optional scale factor for the computed derivative values; by default, no scaling is
.   applied (see #getDerivKernels for details).
.   @param delta optional delta value that is added to the results prior to storing them in dst.
.   @param borderType pixel extrapolation method, see #BorderTypes. #BORDER_WRAP is not supported.
.   @sa  Scharr, Laplacian, sepFilter2D, filter2D, GaussianBlur, cartToPolar
'''
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)
plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()

"""
这是图像扩张和侵蚀之间的区别。
结果将看起来像对象的轮廓。
"""


import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\Admin\Desktop\opencv\j.png')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# img = cv.resize(img, (640, 480))
# 内核大小
kernel = np.ones((5, 5), np.uint8)
# 侵蚀操作
'''
morphologyEx(src, op, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None):
.   @param op Type of a morphological operation, see #MorphTypes
.   @param kernel Structuring element. It can be created using #getStructuringElement.
.   @param anchor Anchor position with the kernel. Negative values mean that the anchor is at the
.   kernel center.
.   @param iterations Number of times erosion and dilation are applied.
.   @param borderType Pixel extrapolation method, see #BorderTypes. #BORDER_WRAP is not supported.
.   @param borderValue Border value in case of a constant border. The default value has a special
.   meaning.
'''
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
cv.imshow('gradient', gradient)
cv.waitKey(0)
cv.destroyAllWindows()

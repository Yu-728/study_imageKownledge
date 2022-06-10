import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\Admin\Desktop\opencv\j.png')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# img = cv.resize(img, (640, 480))
# 内核大小
kernel = np.ones((5, 5), np.uint8)
# 侵蚀操作
'''
dilate(src, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None):
.   @param kernel structuring element used for dilation; if elemenat=Mat(), a 3 x 3 rectangular
.   structuring element is used. Kernel can be created using #getStructuringElement
.   @param anchor position of the anchor within the element; default value (-1, -1) means that the
.   anchor is at the element center.
.   @param iterations number of times dilation is applied.
.   @param borderType pixel extrapolation method, see #BorderTypes. #BORDER_WRAP is not suported.
.   @param borderValue border value in case of a constant border
'''
dilation = cv.dilate(img, kernel, iterations=1)
cv.imshow('dilation', dilation)
cv.waitKey(0)
cv.destroyAllWindows()

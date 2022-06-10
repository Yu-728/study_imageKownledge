import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\Admin\Desktop\opencv\j.png')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# img = cv.resize(img, (640, 480))
# 内核大小
kernel = np.ones((5, 5), np.uint8)
# 侵蚀操作
'''
erode(src, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None):
.   @param kernel 核大小
.   @param anchor 锚点
.   @param iterations 迭代次数
.   @param borderType 像素外推方法，参见#BorderTypes。不支持#BORDER_WRAP。
.   @param borderValue 边界值在边界为常量的情况下
'''
erosion = cv.erode(img, kernel, iterations=1)
cv.imshow('erosion', erosion)
cv.waitKey(0)
cv.destroyAllWindows()

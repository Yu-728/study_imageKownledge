"""
1.使用自适应阈值提取关键信息
2.位运算获取想要的结果
"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 读取图片,灰度处理
img = cv.imread(r'C:\Users\admin\Desktop\test_picture\maomao.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 自适应阈值处理
mask = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                 cv.THRESH_BINARY, 11, 4)
# 二值化处理
# ret, mask = cv.threshold(gray, 220, 255, cv.THRESH_BINARY)

# 临时查看效果
# cv.imshow('original', img)
cv.imshow('mask', mask)
# cv.waitKey()
# cv.destroyAllWindows()

# mask取反
threshold_inv = cv.bitwise_not(mask)
cv.imshow('threshold_inv', threshold_inv)
# and位运算
# result = cv.bitwise_and(img, img, mask=threshold_inv)
# cv.imshow('result', result)
cv.waitKey()
cv.destroyAllWindows()

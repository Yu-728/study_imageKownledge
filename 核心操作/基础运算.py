"""
opencv中加减乘除函数：
add()加法函数 ，subtract()减法函数 ，divide()除法函数，multiply()乘法函数
"""
import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\admin\Desktop\test_picture\maomao.jpg')
rows, clos, channels = img.shape
img1 = np.zeros((rows, clos, channels), dtype=np.uint8)
cv.namedWindow('img1')

a = cv.add(img, img1)
cv.imshow('add', a)
b = cv.subtract(img, img1)
cv.imshow('subtract', b)
c = cv.divide(img, img1)
cv.imshow('divide', c)
d = cv.multiply(img, img1)
cv.imshow('multiply', d)
cv.waitKey()
cv.destroyAllWindows()

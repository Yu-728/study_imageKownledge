"""
目标
了解轮廓是什么。
学习查找轮廓，绘制轮廓等。
你将看到以下功能：cv.findContours()，cv.drawContours()
什么是轮廓?
轮廓可以简单地解释为连接具有相同颜色或强度的所有连续点（沿边界）的曲线。轮廓是用于形状分析以及对象检测和识别的有用工具。

为了获得更高的准确性，请使用二进制图像。因此，在找到轮廓之前，请应用阈值或canny边缘检测。
从OpenCV 3.2开始，findContours()不再修改源图像。
在OpenCV中，找到轮廓就像从黑色背景中找到白色物体。因此请记住，要找到的对象应该是白色，背景应该是黑色。
"""

import numpy as np
import cv2 as cv

# 1.读入图片
img = cv.imread(r'C:\Users\admin\Desktop\test_picture\test.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Otsu二值化处理
ret, thresh = cv.threshold(img_gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

# 2.寻找轮廓
'''
findContours(image, mode, method, contours=None, hierarchy=None, offset=None): 
参数1：源图像
参数2：轮廓的检索方式
参数3：轮廓逼近方法，一般用 cv.CHAIN_APPROX_SIMPLE，就表示用尽可能少的像素点表示轮廓
返回值：
contours：图像轮廓坐标，是一个链表
hierarchy：[Next, Previous, First Child, Parent]
Next：与当前轮廓处于同一层级的下一条轮廓

Previous：与当前轮廓处于同一层级的上一条轮廓

First Child：当前轮廓的第一条子轮廓

Parent：当前轮廓的父轮廓
'''
contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(contours, hierarchy)
print(len(contours), len(hierarchy))

# 3.绘制轮廓
'''
drawContours(image, contours, contourIdx, color, thickness=None, lineType=None, hierarchy=None, maxLevel=None, offset=None):
第一个参数是指明在哪幅图像上绘制轮廓；image为三通道才能显示轮廓
第二个参数是轮廓本身，在Python中是一个list;
第三个参数指定绘制轮廓list中的哪条轮廓，如果是-1，则绘制其中的所有轮廓。
后面的参数很简单。其中thickness表明轮廓线的宽度，如果是-1（cv2.FILLED），则为填充模式。
'''
cv.drawContours(img, contours, -1, (0, 0, 255), 2)

cv.imshow('result', img)
cv.waitKey(0)
cv.destroyAllWindows()

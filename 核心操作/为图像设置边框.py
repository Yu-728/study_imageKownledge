"""
为图像设置边框（填充）
如果要在图像周围创建边框（如相框），则可以使用cv.copyMakeBorder()。
但是它在卷积运算，零填充等方面有更多应用。此函数采用以下参数：
cv2.copyMakeBorder()
    参数：
        img:图像对象
        top,bottom,left,right: 上下左右边界宽度，单位为像素值
        borderType:
            cv2.BORDER_CONSTANT, 带颜色的边界，需要传入另外一个颜色值
            cv2.BORDER_REFLECT, 边缘元素的镜像反射做为边界
            cv2.BORDER_REFLECT_101/cv2.BORDER_DEFAULT
            cv2.BORDER_REPLICATE, 边缘元素的复制做为边界
            CV2.BORDER_WRAP
        value: borderType为cv2.BORDER_CONSTANT时，传入的边界颜色值，如[0,255,0]
"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img1 = cv.imread(r'C:\Users\Admin\Desktop\opencv\jumao-001.jpg')
img = cv.cvtColor(img1, cv.COLOR_BGR2RGB)   # matplotlib的图像是RGB格式
replicate = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_WRAP)
constant = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_CONSTANT, value=[255, 0, 0])
plt.subplot(231), plt.imshow(img), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant), plt.title('CONSTANT')
plt.show()
'''
它的调用是这样子的：
subplot(numbRow ， numbCol ，plotNum ) or  
subplot(numbRow numbCol plotNum)，
解释一下这是啥玩意：
numbRow是plot图的行数；
numbCol是plot图的列数；
plotNum是指第几行第几列的第几幅图 ；
举个例子，如果是subplot (2 ，2 ，1)，那么这个figure就是个2*2的矩阵图，也就是总共有4个图，
1就代表了第一幅图
'''
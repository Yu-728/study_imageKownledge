"""
使用cv.addWeighted函数在文件夹中创建图像的幻灯片放映，并在图像之间进行平滑过渡
实现幻灯片功能
"""

import numpy as np
import cv2 as cv
import time

img1 = cv.imread(r'C:\Users\Admin\Desktop\opencv\changepictuer-project\001.jpg')
img2 = cv.imread(r'C:\Users\Admin\Desktop\opencv\changepictuer-project\002.jpg')
all_image = [img1, img2]
'''
修改图片尺寸为统一大小
统一图片大小参数：
high: 300
wide: 300
channel: 3
'''
# 修改前：
cv.imshow('img1', img1)
cv.imshow('img2', img2)
# 批量显示图片大小
for i in range(len(all_image)):
    print('img%d.shape = ' % i, all_image[i].shape)
'''
如果图片尺寸一样则不需要修改尺寸，否则需要通过cv.resize()更改图片大小
resize(src, dsize, dst=None, fx=None, fy=None, interpolation=None):
src: 原图
dsize: 修改尺寸
dst: 修改后的图
fx: x轴方向缩放因子
fy: y轴方向缩放因子
interpolation: 插值方法
'''
# 图片更改
# dst1 = cv.resize(img1, (300, 300), interpolation=cv.INTER_LINEAR)
'''
初始化窗口显示
'''
i = 0
dst = cv.addWeighted(img2, i, img1, 1 - i, -1)
cv.imshow('ppt', dst)
# 按任意键启动
cv.waitKey(0)
while i < 1.0:
    dst = cv.addWeighted(img2, i, img1, 1 - i, -1)
    cv.imshow('ppt', dst)
    cv.waitKey(80)
    i += 0.1

cv.waitKey(0)
# 按任意键退出
cv.destroyAllWindows()

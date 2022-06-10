"""
使用OpenCV衡量性能
代码计时函数:
**cv.getTickCount**函数返回从参考事件（如打开机器的那一刻）到调用此函数那一刻之间的时钟周期数。
因此，如果在函数执行之前和之后调用它，则会获得用于执行函数的时钟周期数。
**cv.getTickFrequency**函数返回时钟周期的频率或每秒的时钟周期数。
因此，要找到执行时间（以秒为单位）
"""
import numpy as np
import cv2 as cv
import time

'''
cv.getTickCount()使用框架如下：
e1 = cv.getTickCount()
# 你的执行代码
e2 = cv.getTickCount()
time = (e2 - e1) / cv.getTickFrequency()
'''
# cv.getTickCount()使用举例
img1 = cv.imread(r'C:\Users\Admin\Desktop\opencv\changepictuer-project\001.jpg')
e1 = cv.getTickCount()
for i in range(5, 49, 2):
    img1 = cv.medianBlur(img1, i)
e2 = cv.getTickCount()
t1 = (e2 - e1) / cv.getTickFrequency()
print(t1)  # 0.6523605


'''
使time.time()对比
使用框架：
star = time.time()
# 你的执行代码
end = time.time()
'''
start = time.time()
for i in range(5, 49, 2):
    img1 = cv.medianBlur(img1, i)
end = time.time()
t2 = end - start
print(t2)    # 0.6238031387329102

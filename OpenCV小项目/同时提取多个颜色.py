"""
尝试找到一种方法来提取多个彩色对象，例如，同时提取红色，蓝色，绿色对象
"""
import cv2 as cv
import numpy as np

# 读取目标
img = cv.imread(r'C:\Users\Admin\Desktop\opencv\BGR.jpg')
# 转换为HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# hsv颜色提取范围
# 红
lower_red = np.array([0, 43, 46], dtype=np.uint8)
upper_red = np.array([20, 255, 255], dtype=np.uint8)
# 蓝
lower_blue = np.array([106, 43, 46], dtype=np.uint8)
upper_blue = np.array([130, 255, 255], dtype=np.uint8)
# 绿
lower_green = np.array([35, 43, 46], dtype=np.uint8)
upper_green = np.array([77, 255, 255], dtype=np.uint8)
# 设置对应掩膜取对应的颜色
mask_red = cv.inRange(hsv, lower_red, upper_red)
mask_blue = cv.inRange(hsv, lower_blue, upper_blue)
mask_green = cv.inRange(hsv, lower_green, upper_green)
# 掩膜相加，多颜色识别
mask = mask_red + mask_blue + mask_green
# 将掩膜和图像逐像素相加
res = cv.bitwise_and(img, img, mask=mask)
# 显示
cv.imshow('res', res)
cv.waitKey(0)
cv.destroyAllWindows()

import numpy as np
import cv2 as cv

image = cv.imread(r'C:\Users\Admin\Desktop\opencv\jumao-001.jpg')
'''
访问和修改像素值:

你可以通过行和列坐标来访问像素值。
对于 BGR 图像，它返回一个由蓝色、绿色和红色值组成的数组。
对于灰度图像，只返回相应的灰度。
px = image[x, y]  -> 获取图像中x行，y列的像素值，BGR返回（blue, green, red），grad返回灰度值
px = image[x, y, number]
x: 行坐标
y: 列坐标
number: 取值范围0~2，既对应通道的返回值
        0：blue, 1: green, 2: red
'''
px = image[100, 100]
print(px)
# 仅访问蓝色像素
blue = image[100, 100, 0]
print(blue)
print(image.item(100, 100, 0))
'''
使用numpy修改图像像素值,此方法用于修改一整行或者一整列的像素值
不适合单个像素值修改！
Numpy是用于快速数组计算的优化库。
因此，简单地访问每个像素值并对其进行修改将非常缓慢，因此不建议使用
'''
image[100] = [255, 255, 255]    # 第100行的BGR值设置为255
print(image[100, 100])
print(image[90, 100])
'''
注意 上面的方法通常用于选择数组的区域，例如前5行和后3列。
对于单个像素访问，Numpy数组方法array.item()和array.itemset())被认为更好，但是它们始终返回标量。
如果要访问所有B，G，R值，则需要分别调用所有的array.item()
'''
# 访问 RED 值
image.item(10, 10, 2)
# 修改 RED 值
image.itemset((10, 10, 2), 100)
image.item(10, 10, 2)
'''
访问图像属性
图像属性包括行数，列数和通道数，图像数据类型，像素数等。
'''
# image.shape,它返回行，列和通道数的元组（如果图像是彩色的）
print(image.shape)
# 像素总数访问 image.size
print(image.size)
# 图像数据类型 image.dtype
print(image.dtype)
'''
图像感兴趣区域ROI
'''
#          左上坐标   右下坐标
eye = image[140:60, 175:85]
image[10:10, 50:50] = eye
cv.imshow('image', image)
'''
拆分和合并图像通道
cv.split()是一项耗时的操作（就时间而言）。
因此，仅在必要时才这样做。否则请进行Numpy索引
'''
b, g, r = cv.split(image)   # 拆分为blue，green，red
image = cv.merge((b, g, r))     # 合
# 或者
b = image[:, :, 0]  # 拆出blue通道，其他通道类似


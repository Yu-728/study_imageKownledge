"""
学习将不同的几何变换应用到图像上，如平移、旋转、仿射变换等。
函数: cv.getPerspectiveTransform
变换
OpenCV提供了两个转换函数**cv.warpAffine**和**cv.warpPerspective**，您可以使用它们进行各种转换。
**cv.warpAffine**采用2x3转换矩阵，而**cv.warpPerspective**采用3x3转换矩阵作为输入。
"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

'''
缩放
缩放只是调整图像的大小。为此，OpenCV带有一个函数**cv.resize()。
图像的大小可以手动指定，也可以指定缩放比例。也可使用不同的插值方法。
首选的插值方法是**cv.INTER_AREA**用于缩小，**cv.INTER_CUBIC（慢）和**cv.INTER_LINEAR**用于缩放。
默认情况下，出于所有调整大小的目的，使用的插值方法为**cv.INTER_LINEAR**。
resize(src, dsize, dst=None, fx=None, fy=None, interpolation=None):
src: 原图
dsize: 修改尺寸
dst: 修改后的图，缺省
fx: x轴方向缩放因子，缺省
fy: y轴方向缩放因子，缺省
interpolation: 插值方法建议为cv.INTER_LINEAR
'''
img = cv.imread(r'C:\Users\Admin\Desktop\opencv\jumao-001.jpg')
res1 = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)
cv.imshow('res1', res1)
# 或者
height, width = img.shape[:2]  # 取img.shape返回参数中前两个
print(img.shape[:3])  # 取img.shape返回参数中的前3个
print(img.shape[:4])  # 取img.shape返回参数中的前4个,但只有3个返回参数因此只取3个
res2 = cv.resize(img, (2 * width, 2 * height), interpolation=cv.INTER_CUBIC)
cv.imshow('res2', res2)
'''
平移
在平移时要先把图像转换为灰度值
平移是物体位置的移动。如果您知道在(x,y)方向上的位移，则将其设为(tx,ty)，你可以创建转换矩阵M，如下所示：
M=[[1 0 tx][0 1 ty]]
您可以将其放入**np.float32**类型的Numpy数组中，并将其传递给**cv.warpAffine**函数。

warpAffine(src, M, dsize, dst=None, flags=None, borderMode=None, borderValue=None): 
src: 输入
M: 变换矩阵
disize: 输出图片尺寸
**cv.warpAffine**函数的第三个参数是输出图像的大小，其形式应为(width，height)。
width =列数，height =行数
'''
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
rows, cols = img.shape[:2]  # 只取前两个参数，不取通道值
print(rows, cols)
M1 = np.float32([[1, 0, 100], [0, 1, 50]])
dst1 = cv.warpAffine(img, M1, (cols, rows))
cv.imshow('dst1', dst1)
'''
旋转
图像旋转角度为θ是通过以下形式的变换矩阵实现的：
M=[cosθ−sinθsinθcosθ]
但是OpenCV提供了可缩放的旋转以及可调整的旋转中心，因此您可以在自己喜欢的任何位置旋转。修改后的变换矩阵为
[[α β (1−α)*center*x−β*center*y][−β α β*center*x+(1−α)*center*y]]
其中：
α=scale*cosθ, β=scale*sinθ
为了找到此转换矩阵，OpenCV提供了一个函数**cv.getRotationMatrix2D**。
getRotationMatrix2D(center, angle, scale):
center: 旋转中心
angle: 角度
scale: 比例因子
请检查以下示例，该示例将图像相对于中心旋转90度而没有任何缩放比例。
'''
M2 = cv.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), 90, 1)
dst2 = cv.warpAffine(img, M2, (cols, rows))
cv.imshow('dst2', dst2)
'''
透视变换
对于透视变换，您需要3x3变换矩阵。
即使在转换后，直线也将保持直线。要找到此变换矩阵，您需要在输入图像上有4个点，在输出图像上需要相应的点。
在这四个点中，其中三个不应共线。
然后可以通过函数**cv.getPerspectiveTransform**找到变换矩阵。
getPerspectiveTransform(src, dst, solveMethod=None):
功能: 计算从四对对应点的透视变换的矩阵
src: 源图像中四边形顶点的坐标。
dst: 目标图像中相应四边形顶点的坐标。
然后将**cv.warpPerspective**应用于此3x3转换矩阵。
warpPerspective(src, M, dsize, dst=None, flags=None, borderMode=None, borderValue=None):

'''
pts1 = np.float32([[50, 50], [250, 50], [150, 50], [150, 250]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
M = cv.getPerspectiveTransform(pts1, pts2)
dst = cv.warpPerspective(img, M, (300, 300))
plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()

"""
通过将图像与低通滤波器内核进行卷积来实现图像模糊。这对于消除噪音很有用。
它实际上从图像中消除了高频部分（例如噪声，边缘）。
因此，在此操作中边缘有些模糊。（有一些模糊技术也可以不模糊边缘）。
OpenCV主要提供四种类型的模糊技术:
1.平均 2.高斯模糊 3.中位模糊 4.双边滤波
"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread(r'C:\Users\Admin\Desktop\opencv\roi.jpg')
'''
1.平均
这是通过将图像与归一化框滤镜进行卷积来完成的。它仅获取内核区域下所有像素的平均值，并替换中心元素。
这是通过功能**cv.blur()或**cv.boxFilter()完成的。
检查文档以获取有关内核的更多详细信息。我们应该指定内核的宽度和高度。
3x3归一化框式过滤器如下所示：
K = 1/9[ [1 1 1
          1 1 1
          1 1 1] ]
注意 如果您不想使用标准化的框式过滤器，请使用**cv.boxFilter()**。将参数normalize = False传递给函数。
函数：blur(src, ksize, dst=None, anchor=None, borderType=None):

.   @param ksize 模糊核大小
.   @param anchor 锚点;默认值Point(-1，-1)表示锚点位于内核中心。
.   @param borderType 边框模式用于推断图像外的像素，参见#BorderTypes。不支持#BORDER_WRAP。
'''
blur = cv.blur(img, (5, 5))                     # 平均滤波
'''
2.高斯模糊
在这种情况下，代替盒式滤波器，使用了高斯核。
这是通过功能**cv.GaussianBlur()** 完成的。
我们应指定内核的宽度和高度，该宽度和高度应为正数和奇数。
我们还应指定X和Y方向的标准偏差，分别为sigmaX和sigmaY。如果仅指定sigmaX，则将sigmaY与sigmaX相同。
如果两个都为零，则根据内核大小进行计算。高斯模糊对于从图像中去除高斯噪声非常有效。
如果需要，可以使用函数**cv.getGaussianKernel()** 创建高斯内核。
函数： GaussianBlur(src, ksize, sigmaX, dst=None, sigmaY=None, borderType=None):

.   @param ksize 高斯核的大小。核宽度和核高度可以不同，但都必须是正奇数。或者，它们可以是0。由计算得到。
.   @param sigmaX X方向上的高斯核标准偏差。
.   @param sigmaY Y方向高斯核标准差;如果sigmaY为零，则设为sigmaX，
    如果两个都为零，则高斯核核高和核宽由计算得到，分别(详见#getGaussianKernel);
    为了完全控制结果，而不考虑将来可能对所有这些语义进行的修改，建议指定所有的ksize、sigmaX和sigmaY。
.   @param borderType pixel extrapolation method, see #BorderTypes. #BORDER_WRAP is not supported.
.   
'''
GaussianBlur = cv.GaussianBlur(img, (5, 5), 0)  # 高斯模糊函数
'''
3.中位模糊
在这里，函数**cv.medianBlur()** 提取内核区域下所有像素的中值，并将中心元素替换为该中值。
这对于消除图像中的椒盐噪声非常有效。有趣的是，在上述过滤器中，中心元素是新计算的值，该值可以是图像中的像素值或新值。
但是在中值模糊中，中心元素总是被图像中的某些像素值代替。有效降低噪音。其内核大小应为正奇数整数。

函数： medianBlur(src, ksize, dst=None):
.   @param ksize 孔径线性尺寸;它必须是正奇数且大于1，例如:3,5,7…
'''
medianBlur = cv.medianBlur(img, 5)                  # 中位模糊
'''
cv.bilateralFilter() 在去除噪声的同时保持边缘清晰锐利非常有效。但是，与其他过滤器相比，该操作速度较慢。
我们已经看到，高斯滤波器采用像素周围的邻域并找到其高斯加权平均值。
高斯滤波器仅是空间的函数，也就是说，滤波时会考虑附近的像素。
它不考虑像素是否具有几乎相同的强度。它不考虑像素是否是边缘像素。因此它也模糊了边缘，这是我们不想做的。
双边滤波器在空间中也采用高斯滤波器，但是又有一个高斯滤波器，它是像素差的函数。
空间的高斯函数确保仅考虑附近像素的模糊，而强度差的高斯函数确保仅考虑强度与中心像素相似的那些像素的模糊。
由于边缘的像素强度变化较大，因此可以保留边缘。

函数：bilateralFilter(src, d, sigmaColor, sigmaSpace, dst=None, borderType=None):

.   @param d 滤波期间使用的每个像素邻域的直径。如果非正，则从sigmspace计算。
.   @param sigmaColor 在颜色空间中过滤sigma。该参数的值越大，意味着像素邻域(参见sigmspace)中更远的颜色将被混合在一起，
    从而产生更大的半等色区域。
.   @param sigmaSpace 在坐标空间中过滤。参数值越大，表示距离较远的像素将相互影响，只要它们的颜色足够接近(参见sigmaColor)。
    当d\>0时，它指定邻域大小而不考虑sigmspace。否则，d与sigmspace成比例。
.   @param borderType 边框模式用于推断图像外的像素，参见#BorderTypes

'''
bilateralFilter = cv.bilateralFilter(img, 9, 75, 75)       # 双边滤波

cv.imshow('img', img)
cv.imshow('burl', blur)
cv.imshow('GaussianBlur', GaussianBlur)
cv.imshow('medianBlur', medianBlur)
cv.imshow('bilateralFilter', bilateralFilter)
key = cv.waitKey()
# 按任意键退出
cv.destroyAllWindows()

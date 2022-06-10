"""
目标
学习图像金字塔 - 我们将使用图像金字塔创建一个新的水果“Orapple” - 学习以下功能：cv.pyrUp()，cv.pyrDown()

理论
通常，我们过去使用的是恒定大小的图像。但是在某些情况下，我们需要使用不同分辨率的（相同）图像。
例如，当在图像中搜索某些东西（例如人脸）时，我们不确定对象将以多大的尺寸显示在图像中。
在这种情况下，我们将需要创建一组具有不同分辨率的相同图像，并在所有图像中搜索对象。
这些具有不同分辨率的图像集称为“图像金字塔”（因为当它们堆叠在底部时，最高分辨率的图像位于顶部，最低分辨率的图像位于顶部时，看起来像金字塔）。
有两种图像金字塔。1）高斯金字塔   2）拉普拉斯金字塔
高斯金字塔中的较高级别（低分辨率）是通过删除较低级别（较高分辨率）图像中的连续行和列而形成的。
然后，较高级别的每个像素由基础级别的5个像素的贡献与高斯权重形成。通过这样做，
M×N图像变成M/2×N/2图像。
因此面积减少到原始面积的四分之一。它称为Octave。
当我们在金字塔中越靠上时（即分辨率下降），这种模式就会继续。
同样，在扩展时，每个级别的面积变为4倍。我们可以使用**cv.pyrDown**()和**cv.pyrUp**()函数找到高斯金字塔。

"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread(r'C:\Users\admin\Desktop\OpenCV\messi5.jpg')
'''
pyrDown(src, dst=None, dstsize=None, borderType=None):

.   @param dstsize size of the output image.
.   @param borderType 边缘处理, see #BorderTypes (#BORDER_CONSTANT isn't supported)
'''
lower_reso = cv.pyrDown(img)
lower_reso2 = cv.pyrDown(lower_reso)
'''
pyrUp(src, dst=None, dstsize=None, borderType=None):
.   @param dstsize size of the output image.
.   @param borderType Pixel extrapolation method, see #BorderTypes (only #BORDER_DEFAULT is supported)
'''
higher_reso2 = cv.pyrUp(img)
# # BGR-->RGB
# img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# lower_reso = cv.cvtColor(lower_reso, cv.COLOR_BGR2RGB)
# # 显示方式一
# plt.subplot(1, 2, 1), plt.imshow(img), plt.title('Original')
# plt.subplot(1, 2, 2), plt.imshow(lower_reso), plt.title('lower_reso')
plt.show()
# 显示方式二
cv.imshow('img', img)
cv.imshow('lower_reso', lower_reso)
cv.imshow('lower_reso2', lower_reso2)
cv.imshow('higher_reso2', higher_reso2)
cv.waitKey()
cv.destroyAllWindows()

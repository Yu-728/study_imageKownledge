"""
学习如何将图像从一个色彩空间转换到另一个，像BGR↔灰色，BGR↔HSV等
学习以下功能：cv.cvtColor，**cv.inRange**等。
OpenCV中有超过150种颜色空间转换方法。只有两个最广泛使用的,BGR↔灰色和BGR↔HSV。
对于颜色转换，我们使用cv函数。cvtColor(input_image, flag)，其中flag决定转换的类型。
对于BGR→灰度转换，我们使用标志cv.COLOR_BGR2GRAY。类似地，对于BGR→HSV，
我们使用标志cv.COLOR_BGR2HSV。要获取其他标记，只需在Python终端中运行以下命令:
import cv2 as cv
flags = [i for i in dir(cv) if i.startswith('COLOR_')]
print( flags )
ps: HSV的色相范围为[0,179]，饱和度范围为[0,255]，亮度值范围为[0,255]。
不同的软件使用不同的规模。因此，如果你要将OpenCV值和它们比较，你需要将这些范围标准化。
"""
# 举例从摄像头获取人脸区域，图像识别基础
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
while 1:
    '''
    获取摄像头读取帧
    ret: frame = cap.read()
    ret: 为True 或者False,代表有没有读取到图片
    frame: 表示截取到一帧的图片
    '''
    # 读取帧
    ret, frame = cap.read()
    # 翻转图像
    frame = cv.flip(frame, 1)
    '''
    图像颜色转换函数：
    cvtColor(src, code, dst=None, dstCn=None)
    src: 输入图像
    code: 颜色空间转换，例如：cv.COLOR_BGR2HSV 表示：BGE -> HSV
    dst: 输出图像，为缺省参数
    dstCn: 输出图像的通道数，缺省参数
    '''
    # 转换颜色空间 BGR 到 HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    cv.imshow('hsv', hsv)
    # 定义HSV中肤色的范围
    lower_skin = np.array([0, 28, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    '''
    检查数组元素是否位于其他两个数组的元素之间
    OpenCV中的inRange()函数可实现二值化功能（这点类似threshold()函数），更关键的是可以同时针对多通道进行操作，使用起来非常方便！
    主要是将在两个阈值内的像素值设置为白色（255），而不在阈值区间内的像素值设置为黑色（0），该功能类似于之间所讲的双阈值化操作。
    inRange(src, lowerb, upperb, dst=None)
    scr: 输入
    lowerb: 下界数组
    upperb: 上界数组
    dst: 输出，缺省参数
    '''
    # 设置HSV的阈值使得只取肤色
    mask = cv.inRange(hsv, lower_skin, upper_skin)
    # 将掩膜和图像逐像素做与运算
    res = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()

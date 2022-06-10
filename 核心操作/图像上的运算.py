import numpy as np
import cv2 as cv

'''
处理图像运算
OpenCV加法和Numpy加法之间有区别：
OpenCV加法是饱和运算，而Numpy加法是模运算。
'''
x = np.uint8([250])
y = np.uint8([10])
print(cv.add(x, y))  # 250 + 10 = 260 -> 255, np像素数组溢出自动变成255（满像素）
print(x + y)  # 250 + 10 = 260 % 256 = 4
'''
图像融合
这也是图像加法，但是对图像赋予不同的权重，以使其具有融合或透明的感觉。
根据以下等式添加图像:
G(x) = (1−α) * f0(x) + α * f1(x)
通过从 α 从 0→1更改，您可以在一个图像到另一个图像之间执行很酷的过渡。
********** PS: 融合的两幅图片分辨率大小和通道需要相同 ************
在这里，我拍摄了两个图像，将它们融合在一起。第一幅图像的权重为0.7，第二幅图像的权重为0.3。
cv.addWeighted()在图像上应用以下公式:
dst = α * img1 + β * img2 + γ
在这里，γ 被视为零。
'''
# 图像融合例子
img1 = cv.imread(r'C:\Users\Admin\Desktop\opencv\jumao-002.jpg')
img2 = cv.imread(r'C:\Users\Admin\Desktop\opencv\jumao-001.jpg')
dst = cv.addWeighted(img1, 0.2, img2, 0.8, 0)
cv.imshow('dst', dst)
cv.waitKey(0)
cv.destroyAllWindows()

'''
按位运算
这包括按位 AND、 OR、NOT 和 XOR 操作。
bitwise_and bitwise_or  bitwise_not bitwise_xor
它们在提取图像的任何部分(我们将在后面的章节中看到)、定义和处理非矩形 ROI 等方面非常有用。
'''
# 加载两张图片
image1 = cv.imread(r'C:\Users\Admin\Desktop\opencv\roi.jpg')
image2 = cv.imread(r'C:\Users\Admin\Desktop\opencv\jumao-001.jpg')
# print(image2.shape)
# print(image2)           # 最外围矩阵[]表示图像像素矩阵，[[]]:内层矩阵表示第几行，[[[]]]:最内层矩阵表示RGB值和第几列
# print(image2[0, 0])     # [31 36 37]
# print(image2[1, 0])     # [34 39 40]
# print(image2[0, 279])   # [20 21 17]
# print(image2[185, 279])  # [67 99 128]
# print(image2[0, 0, 0])      # 读取图像第0行第0列像素点BGR中的Blue值：31
# print(image2.item(0, 0, 0))     # 读取图像第0行第0列像素点BGR中的Blue值：31
# 我想把image2放在左上角，所以我创建了ROI
rows, cols, channels = image2.shape
roi = image1[0:rows, 0:cols]
# 现在创建image2的掩膜（mask），并同时创建其相反掩膜（mask）
image2gray = cv.cvtColor(image2, cv.COLOR_BGR2GRAY)
'''
图像二值化：
定义：图像的二值化，就是将图像上的像素点的灰度值设置为0或255，
也就是将整个图像呈现出明显的只有黑和白的视觉效果。
灰度值0：黑  灰度值255：白
一幅图像包括目标物体、背景还有噪声，要想从多值的数字图像中直接提取出目标物体，
常用的方法就是设定一个阈值T，用T将图像的数据分成两部分：
大于T的像素群和小于T的像素群。
这是研究灰度变换的最特殊的方法，称为图像的二值化（Binarization）。

ret, dst = cv.threshold( src, thresh, maxval, type[, dst] ) 
参数说明：
src：原图像。
dst：结果图像。
thresh：当前阈值。
maxVal：最大阈值，一般为255.
thresholdType:阈值类型，主要有下面几种：
enum ThresholdTypes {
    THRESH_BINARY     = 0,  大于阈值的部分被置为255，小于部分被置为0
    THRESH_BINARY_INV = 1,  大于阈值部分被置为0，小于部分被置为255
    THRESH_TRUNC      = 2,  大于阈值部分被置为threshold，小于部分保持原样
    THRESH_TOZERO     = 3,  小于阈值部分被置为0，大于部分保持不变
    THRESH_TOZERO_INV = 4,  大于阈值部分被置为0，小于部分保持不变 
    THRESH_MASK       = 7,
    THRESH_OTSU       = 8,
    THRESH_TRIANGLE   = 16
};
返回值:
ret： 与参数thresh一致
dst： 结果图像
使用了THRESH_OTSU和THRESH_TRIANGLE两个标志时，输入图像必须为单通道。
'''
ret, mask = cv.threshold(image2gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('mask', mask)
# print('***********')
# print(mask)
'''
bitwise_not(src, dst=None, mask=None)
功能： 反转数组的每一位
src: 输入
dst: 输出，缺省
mask: 掩码，缺省
'''
# 取反
mask_inv = cv.bitwise_not(mask)
cv.imshow('mask_inv', mask_inv)
# print('************')
# print(mask_inv)
'''
bitwise_and(src1, src2, dst=None, mask=None):
scr1: 输入数组1
scr2: 输入数组2
dst: 输出，缺省
mask: 可选的操作掩码，8位单通道数组，指定要更改的输出数组的元素。
'''
# 现在将ROI中的区域涂黑
image1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)
cv.imshow('image1_bg', image1_bg)
# 仅从logo图像中提取区域
image2_fg = cv.bitwise_and(image2, image2, mask=mask)
cv.imshow('image2_fg', image2_fg)
# 将logo放入ROI并修改主图像
dst = cv.add(image1_bg, image2_fg)
cv.imshow('dst', dst)
image1[0:rows, 0:cols] = dst
cv.imshow('res', image1)
cv.waitKey(0)
cv.destroyAllWindows()

import numpy as np
import cv2 as cv

img = cv.imread(r'C:\Users\admin\Desktop\test_picture\maomao.jpg', 0)
ret, thresh = cv.threshold(img, 127, 255, 0)
'''
def findContours(image, mode, method, contours=None, hierarchy=None, offset=None):
@param mode Contour retrieval mode, see #RetrievalModes     轮廓检索模式
@param method Contour approximation method, see #ContourApproximationModes     轮廓近似法
return： 
        contours：图像轮廓坐标，是一个链表, 多个轮廓的坐标值
        hierarchy：[Next, Previous, First Child, Parent]
            Next：与当前轮廓处于同一层级的下一条轮廓    
            Previous：与当前轮廓处于同一层级的上一条轮廓    
            First Child：当前轮廓的第一条子轮廓
            Parent：当前轮廓的父轮廓
'''
contours, hierarchy = cv.findContours(thresh, 1, 2)
# print(contours)
# print('---------------------------')
# print(hierarchy)
cnt = contours[0]
# cnt1 = contours[1]
# print(cnt)
# print(cnt1)
# print('============================')
'''
def moments(array, binaryImage=None):
@param array Raster image (single-channel, 8-bit or floating-point 2D array) or
       an array (\f$1 \times N\f$ or \f$N \times 1\f$ ) of 2D points (Point or Point2f ).
@param binaryImage If it is true, all non-zero image pixels are treated as 1's. 
       The parameter isused for images only.
return: 返回质心坐标
'''
M = cv.moments(cnt)
print(M)
# 质心
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])
# print(cx, cy)
# 轮廓面积
area = cv.contourArea(cnt)
# print(area)
# 轮廓周长
# 也称为弧长。可以使用**cv.arcLength**()函数找到它。第二个参数指定形状是闭合轮廓(True)还是曲线。
perimeter = cv.arcLength(cnt, True)
# print(perimeter)
# 轮廓近似
# 根据我们指定的精度，它可以将轮廓形状近似为顶点数量较少的其他形状。它是Douglas-Peucker算法的实现。
epsilon = 0.1 * cv.arcLength(cnt, True)
approx = cv.approxPolyDP(cnt, epsilon, True)
# 轮廓凸包
'''
def convexHull(points, hull=None, clockwise=None, returnPoints=None):
参数详细信息：
@param  points: 点**是我们传递到的轮廓。 
@param  hull: **凸包**是输出，通常我们忽略它。 
@param  clockwise: **顺时针方向：方向标记。如果为True，则输出凸包为顺时针方向。否则，其方向为逆时针方向。
@param  returnPoints：默认情况下为True。然后返回凸包的坐标。如果为False，则返回与凸包点相对应的轮廓点的索引
'''
hull = cv.convexHull(cnt, returnPoints=True)  # True返回对应凸包的坐标值
hull1 = cv.convexHull(cnt, returnPoints=False)  # False返回对应凸包的索引值
'''
hull数据解析例子：
首先，我发现它的轮廓为cnt。现在，我发现它的带有returnPoints = True的凸包
得到以下值：[[[234 202]]，[[51 202]]，[[51 79]]，[[234 79]]]，它们是四个角 矩形的点
现在，如果对returnPoints = False执行相同的操作，则会得到以下结果：[[129]，[67]，[0]，[142]],这些是轮廓中相应点的索引。
例如，检查第一个值：cnt [129] = [[234，202]]与第一个结果相同（对于其他结果依此类推）。
'''
# print(hull)
# print(hull1)

# 检查凸度
'''
cv.isContourConvex()具有检查曲线是否凸出的功能。它只是返回True还是False。
'''
k = cv.isContourConvex(cnt)

# 直角矩形
'''
它是一个矩形，不考虑物体的旋转。所以边界矩形的面积不是最小的。它是由函数**cv.boundingRect**()找到的。
令(x，y)为矩形的左上角坐标，而(w，h)为矩形的宽度和高度
'''
x, y, w, h = cv.boundingRect(cnt)
cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#  旋转矩形
'''
这里，边界矩形是用最小面积绘制的，所以它也考虑了旋转。使用的函数是**cv.minAreaRect**()。
它返回一个Box2D结构，其中包含以下细节 -(中心(x,y)，(宽度，高度)，旋转角度)。
但要画出这个矩形，我们需要矩形的四个角。它由函数**cv.boxPoints**()获得
'''
rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(img, [box], 0, (0, 0, 255), 2)
# 最小闭合圈
'''
接下来，使用函数**cv.minEnclosingCircle(*()查找对象的圆周。它是一个以最小面积完全覆盖物体的圆。
def minEnclosingCircle(points):
@param points 轮廓list
return: (x, y)圆心，radius半径
'''
(x, y), radius = cv.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
cv.circle(img, center, radius, (0, 255, 0), 2)
# 拟合一个椭圆
# 下一个是把一个椭圆拟合到一个物体上。它返回内接椭圆的旋转矩形。
ellipse = cv.fitEllipse(cnt)
cv.ellipse(img, ellipse, (0, 255, 0), 2)
# 拟合直线
# 同样，我们可以将一条直线拟合到一组点。下图包含一组白点。我们可以近似一条直线。
rows, cols = img.shape[:2]
[vx, vy, x, y] = cv.fitLine(cnt, cv.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x * vy / vx) + y)
righty = int(((cols - x) * vy / vx) + y)
cv.line(img, (cols - 1, righty), (0, lefty), (0, 255, 0), 2)

#
cv.imshow('results', img)
cv.waitKey()
cv.destroyAllWindows()

import numpy as np
import cv2 as cv

img = cv.imread(r'C:\Users\admin\Desktop\test_picture\maomao.jpg', 0)
ret, thresh = cv.threshold(img, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, 1, 2)
cnt = contours[0]

# 长宽比（高度与宽度的比值）
x, y, w, h = cv.boundingRect(cnt)
aspect_ratio = float(w) / h
# 范围(范围是轮廓区域与边界矩形区域的比值)
area = cv.contourArea(cnt)
rect_area = w * h
extent = float(area) / rect_area
# 坚实度(坚实度是等高线面积与其凸包面积之比)
hull = cv.convexHull(cnt)
hull_area = cv.contourArea(hull)
solidity = float(area) / hull_area
# 等效直径(等效直径是面积与轮廓面积相同的圆的直径)
area = cv.contourArea(cnt)
equi_diameter = np.sqrt(4 * area / np.pi)
#  取向(取向是物体指向的角度。以下方法还给出了主轴和副轴的长度)
(x1, y1), (MA, ma), angle = cv.fitEllipse(cnt)
# 掩码和像素点(在某些情况下，我们可能需要构成该对象的所有点)
mask = np.zeros(img.shape, np.uint8)
cv.drawContours(mask, [cnt], 0, 255, -1)
# pixelpoints = np.transpose(np.nonzero(mask))      #numpy
pixelpoints = cv.findNonZero(mask)  # opencv
# 最大值，最小值和它们的位置
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(img, mask=mask)
# 平均颜色或平均强度(在这里，我们可以找到对象的平均颜色。或者可以是灰度模式下物体的平均强度。我们再次使用相同的掩码进行此操作)
mean_val = cv.mean(img, mask=mask)
# 极端点(极点是指对象的最顶部，最底部，最右侧和最左侧的点)
leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])

import numpy as np
import cv2 as cv

'''
opencv常用画图方法
'''

# 创建黑色的图像
img = np.zeros((512, 512, 3), np.uint8)
# 绘制一条厚度为5的蓝色对角线
#       窗口图像名 起点坐标   终点坐标   RGB颜色（蓝色）线宽
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
#           窗口图像名   起点       终点        RGB颜色（绿色） 线宽
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)  # 画法为左上往右下的对角线所形成的矩形
#               圆心       半径   RGB       是否填充
cv.circle(img, (447, 63), 63, (0, 0, 255), 2)  # -1：填充，其他值不填充，作为线宽参数，默认线宽为1
# 绘制多边形
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
# pts = pts.reshape((-1, 1, 2))
# ture:为封闭图形 False:为多段折线，首尾那段不连接
cv.polylines(img, [pts], True, (0, 255, 255))
# 绘制文字
# 字体设置
font = cv.FONT_HERSHEY_SIMPLEX
# 绘制函数 绘制窗口名 绘制内容  起始位置 字体设置 字体大小比例  RGB 绘制线条粗细程度 线性  图像数据原点True为左下角，否则左上角(默认)
cv.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv.LINE_AA)

# 查看图像
cv.imshow('image', img)
k = cv.waitKey(0)
if k == 27:  # 等待ESC退出
    cv.destroyAllWindows()
elif k == ord('s'):  # 等待关键字，保存和退出
    cv.imwrite(r"C:\Users\Admin\Desktop\opencv\draw-001.jpg", img)
    cv.destroyAllWindows()

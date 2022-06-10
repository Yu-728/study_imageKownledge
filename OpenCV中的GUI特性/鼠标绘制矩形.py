import numpy as np
import cv2 as cv

drawing = False  # 如果按下鼠标，则为真
mode = True  # 如果为真，绘制矩形。按 m 键可以切换到曲线
ix, iy = -1, -1


# 鼠标回调函数
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img, (ix, iy), (x, y), (222, 100, 66), -1)
            else:
                cv.circle(img, (x, y), 5, (0, 0, 255), -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            # 绘制最后鼠标左键释放是的坐标点位置
            cv.rectangle(img, (ix, iy), (x, y), (0, 0, 255), 2)
        else:
            cv.circle(img, (x, y), 5, (0, 0, 255), -1)


# 创建黑色图像和窗口，绑定鼠标动作函数
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)
while 1:
    cv.imshow('image', img)
    if cv.waitKey(1) == 27:
        break

cv.destroyAllWindows()

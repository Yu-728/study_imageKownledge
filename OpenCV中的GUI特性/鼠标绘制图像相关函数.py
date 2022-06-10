import numpy as np
import cv2 as cv


# 鼠标回调函数
def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 100, (255, 0, 0), -1)


# 创建一个黑色的图像，一个窗口，并绑定到窗口的功能
'''
dst=np.zeros((height,width,3),np.uint8)
这个里面的3是三个通道的意思
创建黑色图像
'''
img = np.zeros((512, 512, 3), np.uint8)
# 创建一个窗口
cv.namedWindow('image')
'''
setMouseCallback(windowName, onMouse [, param]) -> None
windowName: 窗口名称
onMouse: 鼠标动作函数
'''
cv.setMouseCallback('image', draw_circle)
while 1:
    cv.imshow('image', img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()

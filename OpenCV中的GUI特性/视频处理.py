import numpy as np
import cv2

# 开启摄像头，创建VideoCapture对象，打开摄像头
cap = cv2.VideoCapture(0)
# cap.isOpened(),判断摄像头是否开启
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # 逐帧捕获，这里获取到得图像是镜像的，后续需要对其进行处理
    ret, frame = cap.read()
    # 如果正确读取帧，ret为True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    '''
    对获取到的图像进行处理
    '''
    # 转换图像为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 图像翻转         图像文件 翻转控制代码
    # frame = cv2.flip(frame, 0)  # 0：垂直翻转
    frame = cv2.flip(frame, 1)  # >0：水平翻转
    # frame = cv2.flip(frame, -1)   # <0: 垂直和水平同时翻转

    # 在图像中画出矩形
    cv2.rectangle(frame, (0, 0), (100, 100), (255, 0, 0), 2)
    # 显示结果帧
    cv2.imshow('frame', frame)
    # 按ESC退出
    if cv2.waitKey(1) == 27:
        break

# 释放缓存
cap.release()
# 关闭所有窗口
cv2.destroyAllWindows()

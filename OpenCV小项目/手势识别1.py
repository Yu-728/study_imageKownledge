import math

import cv2
import mediapipe as mp
import time

# 打开计算机自带摄像头
import numpy as np

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()  # 设置参数，详见 hands.py 中的 __init__
mpDraw = mp.solutions.drawing_utils  # 将检测出的手上的标记点连接起来

# 定义时间用于后边的fps计算
pTime = 0
cTime = 0
temp1 = np.zeros(2)
temp2 = np.zeros(2)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # 图像翻转
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 将BGR格式图像转换为RGB
    results = hands.process(imgRGB)  # 对输入图像进行处理，探索图像中是否有手
    # print(results.multi_hand_landmarks)  # 如果有手，输出手所有0~20个标记点的比例坐标，如果没有，输出None
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:  # 捕捉画面中的每一只手
            for index, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)  # 根据比例还原出每一个标记点的像素坐标
                # print(id, cx, cy)  # 根据手上标记点的id打印出其相应所在图像中中的像素位置
                if index == 4:  # 可以根据手上标记点的id获得任意id对应的标记点的信息
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)  # 这里加粗强调了大拇指上的一个标记点
                    temp1[0] = cx  # 拇指顶点坐标
                    temp1[1] = cy
                if index == 8:  # 可以根据手上标记点的id获得任意id对应的标记点的信息
                    temp2[0] = cx  # 食指顶点坐标
                    temp2[1] = cy
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)  # 给画面中的每一只手进行标点、连线的操作

    # 得到fps
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    # 计算食指和拇指的距离
    l = math.sqrt(math.pow((temp1[0] - temp2[0]), 2) + math.pow((temp1[1] - temp2[1]), 2))
    l = int(l)
    print(l)
    # 长度转换音量
    if (l >= 30) and (l <= 190):
        volume = 0.626 * l - 18.75
    else:
        volume = 0
    print(volume)
    # 画面上显示音量
    cv2.putText(img, 'volume:' + str(int(volume)), (10, 150), cv2.FONT_ITALIC, 1, (0, 0, 255), 3)
    # 在画面上显示fps
    cv2.putText(img, 'FPS:' + str(int(fps)), (10, 70), cv2.FONT_ITALIC, 1, (0, 0, 255), 3)
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)  # 自动刷新
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()

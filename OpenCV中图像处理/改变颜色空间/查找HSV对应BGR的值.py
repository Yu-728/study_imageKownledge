"""
如何找到要追踪的HSV值？
可以使用相同的函数**cv.cvtColor()**。
你只需传递你想要的BGR值，而不是传递图像。
例如，要查找绿色的HSV值，请在Python终端中尝试以下命令:
"""
import cv2 as cv
import numpy as np

green = np.uint8([[[0, 255, 0]]])
red = np.uint8([[[0, 0, 255]]])
blue = np.uint8([[[255, 0, 0]]])
hsv_green = cv.cvtColor(green, cv.COLOR_BGR2HSV)
hsv_red = cv.cvtColor(red, cv.COLOR_BGR2HSV)
hsv_blue = cv.cvtColor(blue, cv.COLOR_BGR2HSV)
print(hsv_green)    # [[[60 255 255]]]
print(hsv_red)      # [[[  0 255 255]]]
print(hsv_blue)     # [[[120 255 255]]]

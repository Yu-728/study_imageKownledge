# coding:utf-8

import numpy as np
import cv2
import matplotlib.pyplot as plt

# 加载图片
'''
imread(img_path,flag) 读取图片，返回图片对象
    img_path: 图片的路径，即使路径错误也不会报错，但打印返回的图片对象为None,路径前记得加r
    flag：cv2.IMREAD_COLOR，读取彩色图片，图片透明性会被忽略，为默认参数，也可以传入1
          cv2.IMREAD_GRAYSCALE,按灰度模式读取图像，也可以传入0
          cv2.IMREAD_UNCHANGED,读取图像，包括其alpha通道，也可以传入-1
'''
img = cv2.imread(r"C:\Users\Admin\Desktop\opencv\jumao-001.jpg")

'''
cvtColor()函数，用于在图像中不同的色彩空间进行转换，用于后续处理
'''
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

'''
图像的二值化，就是将图像上的像素点的灰度值设置为0或255，也就是将整个图像呈现出明显的只有黑和白的视觉效果。
cv2.threshold(img, threshold, maxval,type)
threshold是设定的阈值
maxval是当灰度值大于（或小于）阈值时将该灰度值赋成的值
type规定的是当前二值化的方式
'''
ret, img_threshold = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

'''
imshow(window_name,img)：显示图片，窗口自适应图片大小
    window_name: 指定窗口的名字
    img：显示的图片对象
    可以指定多个窗口名称，显示多个图片
'''
cv2.imshow("img", img)
cv2.imshow("thre", img_threshold)

'''
waitKey函数功能是不断刷新图像，频率时间为delay，单位为ms；该函数通常用在显示图像函数之后。
格式： key = waitKey(delay=0);
参数：delay延时时间，单位ms；
delay>0时，延迟"delay"ms；
当delay<=0的时，如果没有键盘触发，则一直等待，否则返回值为键盘按下的码字；
通常: 键盘按键的符号可以使用ord()函数来转换；
它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值；
    
destroyAllWindows(window_name) 
    window_name: 需要关闭的窗口名字，不传入时关闭所有窗口
'''
key = cv2.waitKey(0)
# 按任意键退出
cv2.destroyAllWindows()
'''
imwrite(img_path_name,img)
    img_path_name:保存的文件名,路径前记得加r
    img：文件对象
'''
cv2.imwrite(r"C:\Users\Admin\Desktop\opencv\jumao-003.jpg", img)
cv2.imwrite(r"C:\Users\Admin\Desktop\opencv\jumao-002.jpg", img_threshold)

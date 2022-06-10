"""
Python控制自己的手机摄像头拍照，并把照片自动发送到邮箱
这是一个大佬的项目，本着学习的心态对其进行学习
大佬链接：https://blog.csdn.net/m0_48405781/article/details/124171923?spm=1001.2100.3001.7377&utm_medium=distribute.pc_feed_blog.none-task-blog-personrec_tag-2.nonecase&depth_1-utm_source=distribute.pc_feed_blog.none-task-blog-personrec_tag-2.nonecase
目标：控制自己的摄像头拍照，并且把拍下来的照片，通过邮件发到自己的邮箱里。
思路：
通过opencv调用摄像头拍照保存图像本地
用email库构造邮件内容,保存的图像以附件形式插入邮件内容
用smtplib库发送邮件到指定邮箱
"""
import time
import cv2 as cv
from email.mime.image import MIMEImage  # 用来构造邮件内容的库
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib  # 发送邮件


def GetPicture():
    """
    拍照保存图像
    """
    # 创建一个窗口
    # cv.namedWindow('camera', 1)
    '''
    拍照是用手机的摄像头，软件用的是：IP摄像头（安卓），
    因为在同一个局域网内，打开APP，里面出现的网址就是摄像头的地址
    我这里直接用的电脑的摄像头
    '''
    # 调用摄像头   IP摄像头APP
    # video = ""  # 摄像头地址
    cap = cv.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        frame = cv.flip(frame, 1)
        cv.imshow("camera", frame)
        # 按键处理
        key = cv.waitKey(10)
        if key == 27:
            # 保存
            cv.imwrite(r'E:\SavePicture-camera\001.jpg', frame)
            break

    # 释放摄像头
    cap.release()
    # 关闭窗口
    cv.destroyWindow("camera")


# 授权码
pwd = "gflpeixmuywtghji"  # 最好写自己的

# 服务器接口
host = 'smtp.qq.com'
port = 25

sender = '1835936725@qq.com'  # 最好写自己的
receiver = 'ybl728@163.com'  # 最好写自己的


def SetMsg():
    """
    邮件格式设置
    :return:
    """

    msg = MIMEMultipart('mixed')
    # 标题
    msg['Subject'] = '小姐姐照片'
    msg['From'] = sender  # 发送方邮箱
    msg['To'] = receiver  # 接收方邮箱

    # 邮件正文
    text = '你要的小姐姐照片到了,请接收'
    text_plain = MIMEText(text, 'plain', 'utf-8')  # 正文转码
    msg.attach(text_plain)

    # 图片附件
    SendImageFile = open('E:/SavePicture-camera/001.jpg', 'rb').read()
    image = MIMEImage(SendImageFile)

    # 将收件人看见的附件照片名称改为people.png.
    image['Content-Disposition'] = 'attachment; filename = "people.png"'
    msg.attach(image)
    return msg.as_string()


def SendEmail(msg):
    """
    发送邮件
    :param msg:邮件内容
    :return:
    """
    smtp = smtplib.SMTP()
    smtp.connect(host, port=25)
    smtp.login(sender, pwd)
    smtp.sendmail(sender, receiver, msg)
    time.sleep(2)
    smtp.quit()


if __name__ == '__main__':
    # 1.拍照保存
    GetPicture()
    # 2.设置邮件格式
    msg = SetMsg()
    # 3.发送邮件
    SendEmail(msg)

"""
24位密码
"""

import random
import os

# ASCII码
list_A = [chr(i) for i in range(97, 123)]
list_a = [chr(i) for i in range(65, 91)]
list_1 = [chr(i) for i in range(48, 58)]
list_all = list_1 + list_A + list_a


def get_code():
    temp = []
    for i in range(4):
        s = random.sample(list_all, k=6)  # 返回一个list
        s.append('-')
        for j in s:
            temp.append(j)
    return temp[:len(temp) - 1]  # 把之前多加的-去掉


def code_print(s):
    for i in s:
        print(i, end='')


def text_create(msg):
    for j in msg:
        file = open(r'E:\Python_Code\pythonProject\study_imageKownledge\test\密码本.txt', 'a')
        file.write(str(j))
    file = open(r'E:\Python_Code\pythonProject\study_imageKownledge\test\密码本.txt', 'a')
    file.write('\n')


n = input("请输入需求密码个数：")
n = int(n)
for i in range(n):
    x = get_code()
    code_print(x)
    print('')
    text_create(x)

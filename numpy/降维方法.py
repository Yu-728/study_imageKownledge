"""
numpy中的降维方法：
flat（）：返回一个iterator，然后去遍历
flatten（）：将多维数组拉平，并拷贝一份
ravel（）：将多维数组拉平（一维）
squeeze（）：除去多维数组中，维数为1的维度，如315降维后3*5
reshape（-1）：多维数组，拉平
reshape（-1，5），其中-1表示我们不用亲自去指定这一维度的大小，理解为n维
"""
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

c = []
for x in a.flat:
    c.append(x)
print('flat迭代器降一维：\n', c)
d = a.flatten()
print('flatten方法降一维：\n', d)
e = a.ravel()
print('ravel方法降一维：\n', e)
g = np.squeeze(a)
print('squeeze方法降一维：\n', g)
f = a.reshape(-1)
print('reshape方法降一维：\n', f)
a.resize((1, 6))
print('resize方法：\n', a)

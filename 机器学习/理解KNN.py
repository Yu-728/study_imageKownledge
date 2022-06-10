"""
理论： http://woshicver.com/Ninth/8_1_%E7%90%86%E8%A7%A3KNN/
"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 包含(x,y)值的25个已知/训练数据的特征集
trainData = np.random.randint(0, 100, size=(25, 2)).astype(np.float32)
# 用数字0和1分别标记红色或蓝色
responses = np.random.randint(0, 2, (25, 1)).astype(np.float32)
# 取红色族并绘图
red = trainData[responses.reshape(-1) == 0]
plt.scatter(red[:, 0], red[:, 1], 80, 'r', '^')
# 取蓝色族并绘图
blue = trainData[responses.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 80, 'b', 's')
# 输入
newcomer = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(newcomer[:, 0], newcomer[:, 1], 80, 'g', 'o')
'''
KNN算法（近朱者赤，近墨者黑）分类算法
1）创建 cv2.ml.KNearest_create()；

2）训练 knn.train(train, cv.ml.ROW_SAMPLE, train_labels)；

3）预测 ret,result,neighbours,dist = nn.findNearest(sample,k=5)

sample 是待预测的数据样本；
k 表示选择最近邻的数目；
result 表示预测结果；
neighbours 表示每个样本的前k个邻居；
dist表示每个样本前k的邻居的距离；
'''
# 创建
knn = cv.ml.KNearest_create()
# 训练
knn.train(trainData, cv.ml.ROW_SAMPLE, responses)
# 预测
ret, results, neighbours, dist = knn.findNearest(newcomer, 3)
print("result:  {}\n".format(results))
print("neighbours:  {}\n".format(neighbours))
print("distance:  {}\n".format(dist))
plt.show()

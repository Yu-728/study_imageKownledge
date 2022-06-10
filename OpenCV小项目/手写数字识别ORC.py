"""
OCR（optical character recognition）文字识别是指电子设备（例如扫描仪或数码相机）检查纸上打印的字符，
然后用字符识别方法将形状翻译成计算机文字的过程；即，对文本资料进行扫描，然后对图像文件进行分析处理，获取文字及版面信息的过程。
如何除错或利用辅助信息提高识别正确率，是OCR最重要的课题。
衡量一个OCR系统性能好坏的主要指标有：拒识率、误识率、识别速度、用户界面的友好性，产品的稳定性，易用性及可行性等。
————百度百科
"""
import numpy as np
import cv2 as cv

img = cv.imread(r'E:\opencv-4.5.5\opencv-4.5.5\samples\data\digits.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# print(gray.shape)       # shape(1000, 2000), size = 2000000
# 现在我们将图像分割为5000个单元格，每个单元格为20x20
'''
np.hsplit(row, 100)--->沿垂直方向拆分row矩阵，拆分为100个
np.vsplit(gray, 50)--->沿水平方向拆分gray矩阵，拆分成50个
'''
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
# 使其成为一个Numpy数组。它的大小将是（50,100,20,20）三维
x = np.array(cells)
# 现在我们准备train_data和test_data。
'''
x[:, 0:50]--->取x矩阵中的前50列的元素-->size(50, 50, 20 , 20)
reshape(-1, 400)--->将矩阵转化为400个元素一列的矩阵---->2500*400
test同理
'''
train = x[:, 0:50].reshape(-1, 400).astype(np.float32)  # Size = (2500,400)
test = x[:, 50:100].reshape(-1, 400).astype(np.float32)  # Size = (2500,400)
# 为训练和测试数据创建标签
k = np.arange(10)
train_labels = np.repeat(k, 250)[:, np.newaxis]
test_labels = train_labels.copy()
# 初始化kNN，训练数据，然后使用k = 5的测试数据对其进行测试
knn = cv.ml.KNearest_create()
knn.train(train, cv.ml.ROW_SAMPLE, train_labels)
ret, result, neighbours, dist = knn.findNearest(test, k=5)
# 现在，我们检查分类的准确性
# 为此，将结果与test_labels进行比较，并检查哪个错误
# print(test[0, :])
# print(test[0, :].shape)
# print("result:  {}\n".format(result))
# print("neighbours:  {}\n".format(neighbours))
# print("distance:  {}\n".format(dist))
matches = result == test_labels
correct = np.count_nonzero(matches)
accuracy = correct * 100.0 / result.size
print(accuracy)

# 保存数据
np.savez('knn_data.npz', train=train, train_labels=train_labels)
# 读取保存数据
with np.load('knn_data.npz') as data:
    print(data.files)
    train = data['train']
    # print(train)
    train_labels = data['train_labels']
    # print(train_labels)

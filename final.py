import numpy as np
import matplotlib.pyplot as plt
#导入numpy、matplotlib模块并使用np、plt作为简称

data = [2*i+5 for i in range(200)]
m = 200                                     # sample length（样本大小）

# generate matrix X
# 构建特征矩阵  创建一个m * 2的数组X，第一列全为1，第二列为1~m
X0 = np.ones((m, 1))                         #创建一个全为1的 m * 1 的数组
X1 = np.arange(0, m).reshape(m, 1)         #创建一个从1到m+1（不包括m+1）的数组，再通过 reshape(m, 1) 改变数组的形状为 m * 1
X = np.hstack((X0, X1))                      #将X0和X1数组在列上进行水平拼接，得到一个 m * 2 的数组，X.

# matrix y
y = np.array(data).reshape(m,1)              #将列表data转换成numpy数组,并数组的形状为 m * 1

alpha = 0.0001
# alpha=α  theta=θ
# 定义一个计算代价函数（误差平方和），用来评估线性回归模型的拟合程度
# theta是模型参数，是一个 n * 1 的列向量；X是特征矩阵，是一个 m * n 的矩阵；y是目标变量，它是一个 m * 1 的列向量。
# np.dot(A, B): 矩阵乘法
# np.transpose(array): 转置数组
def cost_function(theta, X, y):
    diff = np.dot(X, theta) - y                #通过矩阵乘法，计算出预测值和真实值之间的差值，并将其赋值给变量diff
    return (1./2*m) * np.dot(np.transpose(diff), diff)     #算出差值的转置矩阵和差值矩阵的点积(也就是差值平方和)，
                                                           # 1./2 表示将浮点数1除以2，结果为0.5  再乘以m(m为样本数，2是因为是平方和)

# 计算梯度函数, 用于更新参数theta
def gradient_function(theta, X, y):
    diff = np.dot(X, theta) - y
    return (1./m) * np.dot(np.transpose(X), diff)

# 执行梯度下降算法，求解线性回归问题的参数解
def gradient_descent(X, y, alpha):
    theta = np.array([1, 1]).reshape(2, 1)               #创建一个初始的 theta 参数矩阵，并将其形状设置为 2 * 1 的矩阵。
    gradient = gradient_function(theta, X, y)            #调用 gradient_function() 函数来计算当前 theta 参数下的梯度
    while not np.all(np.absolute(gradient) <= 1e-5):     #如果所有元素的绝对值都小于等于1e-5，则终止循环
        theta = theta - alpha * gradient                 #更新 theta 参数矩阵，alpha 是学习率=0.0001，gradient 是梯度
        gradient = gradient_function(theta, X, y)        #重新计算梯度
    return theta                                         #返回最终得到的 theta 参数矩阵

[theta0, theta1] = gradient_descent(X, y, alpha)

print(theta0, theta1)

plt.figure()                                    #plt.figure(figsize=(width, height)): 创建一个新的图表，并设置图表的大小
plt.scatter(X1,y)                               #绘制散点图
plt.plot(X1, theta0 + theta1*X1, color='g')     #绘制线图 设置为绿色
plt.title('dddd')                               #设置标题（中文的显示还需要设置什么？）
plt.grid(True)                                  #显示图表的网格
plt.show()                                      #显示图表

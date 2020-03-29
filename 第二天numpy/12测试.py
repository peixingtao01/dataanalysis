import numpy as np
iris = np.genfromtxt('./iris_sepal_length.csv')
# print(iris)
iris = np.unique(iris)
print(iris)

print(np.sum(iris,axis=0))#数组求和
print(np.mean(iris,axis=0))#数组求均值
print(np.std(iris,axis=0))#数组求标准差
print(np.var(iris,axis=0))#数组求方差
print(np.min(iris,axis=0))#数组求最小值
print(np.max(iris,axis=0))#数组求最大值
print(np.argmin(iris,axis=0))#数组求最小元素索引
print(np.argmax(iris,axis=0))#数组求最大元素索引
print(np.cumsum(iris,axis=0))#数组求所有元素的累计和
print(np.cumprod(iris,axis=0))#数组求所有元素的累计积
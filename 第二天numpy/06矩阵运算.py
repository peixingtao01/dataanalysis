import numpy as np

m1 = np.mat(np.arange(4).reshape(2,2))
m2 = np.mat(np.arange(4,8).reshape(2,2))
print(m1)
print(m2)
# print(m1*m2)

mty = np.multiply(m1,m2) #对应元素相乘，必须满足方阵
mt = np.matmul(m1,m2) #只要符合矩阵相乘条件就可以运算
print(mty)
print(mt)


print('矩阵转置：\n',m1.T)
print('矩阵的逆：\n',m1.I)
print('矩阵共轭转置：\n',m1.H)
print('矩阵视图：就是它的数组形式\n',m1.A)

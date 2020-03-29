import numpy as np

# arr = np.arange(16).reshape(4,4)
# 数组展开就是将高维度转化为低维度

arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(arr.ravel())#这个是转化成一行

print(arr.flatten(order="C"))#是按照C形式转化成一行，C是按行展开
print(arr.flatten(order="F"))#是按照F形式转化成一行，F是按列展开



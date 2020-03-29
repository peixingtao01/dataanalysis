import numpy as np
# 数组可以是多维的，但是矩阵只能是二维的

# 创建矩阵使用mat，matrix asmatrix
# 但是mat，asmatrix快
jz_str = np.mat('1 2 3;4 5 6;7 8 9')
print(jz_str)
qt_str = np.mat([[1,2,3],[4,5,6],[7,8,9]])
print(qt_str)
shuzu = np.mat(np.array([[[1,2,3],[4,5,6]]]))#转换成矩阵，可以降维
print(shuzu)
print('='*80)

# 都可以降维
asde = np.asmatrix(np.array([[[1,2,3],[4,5,6]]]))
print(asde)
matt = np.matrix(np.array([[[1,2,3],[4,5,6]]]))
print(matt)
print('='*80)

# bmat 组成范德蒙德，堆积矩阵
arr1 = np.arange(4).reshape(2,2)
arr2 = np.arange(4,8).reshape(2,2)
m2 = np.bmat([[arr1,arr2],[arr2,arr1]])
print(m2)


'''
arr1 = list(np.arange(4).reshape(2,2))
print(arr1)

arr2 = list(np.arange(4,8).reshape(2,2))

'''
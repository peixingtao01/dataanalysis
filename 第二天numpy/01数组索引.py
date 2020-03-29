import numpy as np

arr = np.arange(16)
# print(arr)

# data = arr[4] #4
# print(data)
# print('形状',arr.shape)
# print('维度',arr.ndim)

"""
print(arr[-2])#可以从后向前数
print(arr[3:9:3])#一位数组与列表一致
print(arr[[2, 5,8]])#可以求他们的子集,
"""
arr = arr.reshape(4,4)
# reshape可以是带括号的，也可以是不带括号的
print(arr,end='\n\n')
# print(arr.ndim,end='\n\n\n')

data1 = arr[:,0]#获取第一列
# print(data1)

data2 = arr[[0,2],[0,1]]
# 这个前面获取的是行，后面获取的是列，行列按照逗号进行分割的，然后按照位置一一对应[0 9]
# 这个会返回一个新的数组
# print(data2)

data3 = arr[0::2,1:3]
# print(data3)
'''
[[ 1  2]
 [ 9 10]]
'''


#二维数组取值不可以超出逻辑范围


# arange不支持bool,但是array支持



# 布尔定义筛选条件
arr_mask = np.array([0,1,0,3],dtype=np.bool)
#定义一个筛选条件，然后过滤掉不符合条件的信息，数量要与进行过滤的数组进行数量对应
print(arr_mask)
data4 = arr[arr_mask,arr_mask]
print(data4)
data5 = arr[arr_mask,:]
print(data5)


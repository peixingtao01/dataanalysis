import numpy as np
# 数组组合就是数组拼接


arr1 = np.arange(4).reshape(2,2)
print(arr1)

arr2 = np.arange(4,8).reshape(2,2)
print(arr2)

# new_arr1 = np.vstack(arr1,arr2)直接这样写会报错的，必须在一个元组或者列表之中
# v--是增加了行，h--是增加了列
new_arr1 = np.vstack([arr1,arr2])
new_arr2 = np.hstack([arr1,arr2])
print(new_arr1)
print(new_arr2)
'''
[[0 1]
 [2 3]
 [4 5]
 [6 7]]
 
[[0 1 4 5]
 [2 3 6 7]]
'''

# 可以设置参数进行拼接，默认是增加行。参数是axis，0是按行，1是按列
new_arr_concatenate1 = np.concatenate((arr1,arr2))
new_arr_concatenate2 = np.concatenate((arr1,arr2),axis=0)#按行拼接
new_arr_concatenate3 = np.concatenate((arr1,arr2),axis=1)#按列拼接
print(new_arr_concatenate1)
print(new_arr_concatenate2)
print(new_arr_concatenate3)
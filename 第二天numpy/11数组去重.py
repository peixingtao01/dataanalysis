import numpy as np

# unique不仅可以去掉数组中重复的数字，并且还可以将数组升序排序
arr_1 = np.array([1,2,3,3,2,1,5,6,4,5,7,9])
res_1 = np.unique(arr_1)
# print(res_1)
# unique还可以将数组进行降重，然后进行升序排序
arr_2 = np.arange(4).reshape(2,2)
print(arr_2)
res_2 = np.unique(arr_2)
print(res_2)


# tile将整个数组重复n次，按照列方向进行扩展
res_t = np.tile(arr_2,2)
print(res_t)

# 可以改变方向的整体重复,repeat
# axis=0 按照行进行重复  =1按照列进行重复
res_r = np.repeat(arr_2,2,axis=0)
print(res_r)
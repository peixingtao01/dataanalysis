import numpy as np

arr=np.array([[1,2,3],[4,5,6]])
print(type(arr))#<class 'numpy.ndarray'>

print(arr)

print(arr.ndim)#数组维度  2
print(arr.shape)#数据形状  (2, 3)
print(arr.size)#数组大小  6
print(arr.dtype)#数据类型  int32
print(arr.itemsize)#每个元素实际大小  4

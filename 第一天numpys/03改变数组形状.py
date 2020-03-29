import numpy as np

arr = np.arange(6)
print(arr.shape)
# 改变形状
arr.shape=(2,3)
print(arr.shape)
print(arr)

xx = arr.reshape((3,2))
print(xx)
print(xx.shape)

a = np.arange(6,dtype=np.float64).reshape((3,2))
print(a)
print(a.dtype)

df = np.dtype([('name',np.str_,20),('height',np.float64),('weight',np.float)])
arrs = np.array([('bp',170.0,55.1),('zs',178.2,80.1),('yf',176.2,75.3)],dtype=df)
print(arrs)
print(arrs.dtype)
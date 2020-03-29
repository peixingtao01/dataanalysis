import numpy as np

arr = np.arange(16).reshape(4,4)
print(arr)

#v-h 拆分|拆分时候，必须整除,h按列拆分，v按照行拆分
h_arr = np.hsplit(arr,4)
print(h_arr)
v_arr = np.vsplit(arr,4)
print(v_arr)

# 按照参数切分
hang_arr = np.split(arr,4,axis=0)
print(hang_arr)
lie_arr = np.split(arr,4,axis=1)
print(lie_arr)
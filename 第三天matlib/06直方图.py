import numpy as np
import matplotlib.pyplot as plt

# 1
plt.figure()

# 2 hist.有数相同个数并计数的作用
weight = np.array([40,44,48,46,51,56,58,62,69,75,89,78,69,56,88,57,49,60,50,61])

# 需要设置区间范围，先求出极差，计算区间长度，设置等宽
ptp = weight.max() - weight.min()
step = np.ceil(ptp/4)
bins = np.arange(weight.min(),weight.max()+step,step)
print(bins)
plt.hist(weight,color='c',edgecolor='k',bins=bins)
# bins= 设置区间长度
# color=设置颜色，可以是一个，也可以是一组
# edgecolor= 柱子的边框颜色
plt.grid(True,axis='y',alpha=0.2)
# 3
plt.show()
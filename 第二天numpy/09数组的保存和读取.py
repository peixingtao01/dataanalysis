import numpy as np
arr1 = np.arange(16).reshape(4,4)
arr2 = np.arange(16,32).reshape(4,4)

# 保存和读取
"""
# save保存二进制数，后缀名是.npy
# 这个可以省略文件名后缀
np.save('./save保存的arr',arr1)

# 读取.npy文件，用load读取，需要说明后缀名
arr2 = np.load('./save保存的arr.npy')
print(arr2)

# 一次保存多个数组
np.savez('./savez保存的arr',arr1,arr2)
"""


# 换一种保存格式，保存文本,这种就不是保存二进制数了
# np.savetxt('./savetxt保存的txt.txt',arr1,fmt='%d',delimiter=',')
# np.savetxt('./savetxt保存的csv.csv',arr2,fmt='%d',delimiter=',')
# 读取，读取的时候delimiter参数要与保存时的参数一致，否则会报错
data1 = np.loadtxt('./savetxt保存的txt.txt',dtype=int,delimiter=',')
data2 = np.loadtxt('./savetxt保存的csv.csv',dtype=int,delimiter=',')
print(data1)
print(data2)


# 读取结构化数组，还可以补全缺失的数据
# filling_values就是当你缺失值的时候，它给你补全这个位置的值
data = np.genfromtxt('./savetxt保存的txt.txt',dtype=int,delimiter=',',filling_values='-1')
print(data)
arrx = np.load('./savez保存的arr.npz')
print(arrx)
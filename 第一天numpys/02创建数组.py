import numpy as np
# 创建一维二维数组
arr_1 = np.array([1,2,3]) #一维
arr_2 = np.array([[1,2,3],[4,5,6]]) #二维

# 创建数组，是一维的
# 需要设置开始值 结束值 步长创建一维数组
# --前闭后开
arr_arange = np.arange(1,3,0.5)
print(arr_arange)


# 创建linspace按照等差方法在指定区间内取值
# linspace是等差的创建
arr_lins=np.linspace(0,5,5)
print(arr_lins)
# [ 0.  1.25  2.5  3.75  5.]


# 创建logspace按照等比方法在指定区间取值
arr_log=np.logspace(0,3,3)
# 是按照10的多少次方进行等比的
# 比方说生成10^0  10^1  10^2 这样等比的
print(arr_log)

# 创建zeros函数,
# 创建一个符合传入矩阵形状的二维数组
arr_zeros = np.zeros((3,3))
print(arr_zeros)

# 创建符合传入参数的单位矩阵(数组)
# 其中3，是传入参数，规定了3行3列.
# k是规定偏移量，正数为向上偏移，负数为向下偏移。但是会丢失对角线元素
arr_eye = np.eye(3,k=1)
print(arr_eye)


# 创建一个对角线的矩阵(数组)
# 当然也可以设置偏移量，不过这次不会丢失元素
arr_diag = np.diag([1,2,3,4],k=2)
print(arr_diag)


# 创建元素都是1的数组，传入矩阵形状
arr_ones=np.ones((3,4))
print(arr_ones)


# 创建随机数数组
# 创建一个[0,1)的符合传入参数个数的数组
arr_random = np.random.random(10)
print(arr_random)


# 创建一个符合传入参数几行几列的均匀分布的数组
# 均匀分布应该是按照某种规律进行的分布，是[0,1)的
arr_rand = np.random.rand(3,2)
print(arr_rand)

# 创建一个符合传入参数几行几列的正态分布的数组
arr_randn = np.random.randn(3,2)
print(arr_randn)


# 创建一个符合传入size的，元素区间位于[1,5)的数组
arr_randint = np.random.randint(1,5,size=[3,6])
print(arr_randint)


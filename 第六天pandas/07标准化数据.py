# 标准化数据的目的就是为了让数据转化为同一个数量级,减轻异常值对结果的影响

# 将数据进行变化
# 三种方式
import numpy as np
import pandas as pd
# 离差标准化 (x-min)/(max-min)
def licha(lie):
    data = (lie-lie.min())/(lie.max()-lie.min())
    return data


# 标准差标准化  (x-mean)/std
# lie-平均值/标准差
# 将数据转化为标准差为1，均值为0的状态
def std(lie):
    data = (lie-lie.mean()) / lie.std()
    return data


# 小数定标标准化，就是将所有数据都转化成[0,1]的小数
# x/10^k (k=lg(|x|.max))
# 意思就是这一列中的最大值求出来它的k，然后用所有数据去除这个数
# 就是将小数位数进转化
# 这个是对最终数据影响很小，因为是每个数据进行转换
# 不用管异常值
def desc_sca(lie):
    data = lie/(10**np.ceil(np.log10(lie.abs().max())))
    return data

detail = pd.read_excel("./meal_order_detail.xlsx")
a1 = licha(detail.loc[:,'amounts'])
a2 = std(detail.loc[:,'amounts'])
a3 = desc_sca(detail.loc[:,'amounts'])
print(a1)
print(a2)
print(a3)

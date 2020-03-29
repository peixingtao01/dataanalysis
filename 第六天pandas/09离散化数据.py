# 离散化数据就是为了将非数值型数据(类别型)转化为可操作数据
import pandas as pd
import numpy as np

# 就相当于转化成了一个邻接矩阵
# 先将转化为类别数据
res = pd.read_excel('./meal_order_detail.xlsx')
# print(res.loc[:,"dishes_name"])
# 做成邻接矩阵
# ybl = pd.get_dummies(data=res.loc[:,'dishes_name'],prefix='菜',prefix_sep=':')
# print(ybl)




# 将连续数据进行离散化pd.cut
zf = pd.cut(res.loc[:,'amounts'],bins=5,include_lowest=True)
print(zf)

# 它自己分组就是不如我自己分组，所以我直接传入分组，然后你归类
# 等差分组
ptp = res.loc[:,'amounts'].max() - res.loc[:,'amounts'].min()
step = np.ceil(ptp/5)
bins = np.arange(res.loc[:,'amounts'].min(),res.loc[:,'amounts'].max()+step,step)
dcfz = pd.cut(res.loc[:,"amounts"],bins=bins,include_lowest=True)
print(dcfz)
print('='*80)

# 等频分组
bins = res.loc[:,"amounts"].quantile(np.arange(0,1+0.2,0.2))
dpfz = pd.cut(res.loc[:,'amounts'],bins=bins,include_lowest=True)
print(dpfz)

# 分组计数
res_count = pd.value_counts(dpfz)
print(res_count)
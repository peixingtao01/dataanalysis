import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 所谓的分组聚合，就是先按照某个属性将数据分组，然后将每个组进行计算的操作
res= pd.read_excel('./users.xlsx')
# print(res)
c_list = res.loc[:,'ORGANIZE_NAME']

# 按照班级分组，将每个班的年龄总和求出来
c_names = res.groupby(by='ORGANIZE_NAME')['age'].count()
print(c_names)
print('='*80)


# 按照班级分组，将每个班中每个地区的男女的平均年龄求出来
x = res.groupby(by=['ORGANIZE_NAME','poo','sex'])['age'].mean()
print(x)
print('='*80)

#对一列求和，对另一列求最大值，同时输出
k = res.agg({'age':np.mean,'USER_ID':np.max})
print(k)
print('='*80)

#
t=res.groupby(by='ORGANIZE_NAME')['USER_ID'].count()
print([a for a in t.index])
print([i for i in t])
print('='*80)
"""
plt.figure()
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
plt.pie([i for i in t],labels=[a for a in t.index])
plt.axis('equal')
plt.show()
"""

# 自定义函数apply()
# apply,但是apply更加灵活，也快
# transform只能对一列进行计算
d = res['age'].apply(lambda x:x+1000)
e = res['age'].transform(lambda x:x+2000)
print(d)
print(e)
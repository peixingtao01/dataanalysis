import pandas as pd
import numpy as np

"""
#正态分布
res = pd.read_excel('./meal_order_detail.xlsx',sheetname=0)
print(res.shape)
def sigema(data):
    bl1 = (data.mean()-3*data.std()) <=data
    bl2 = (data.mean()+3*data.std()) >=data
    bools = bl1 & bl2
    # 之所以用&而不是and，是因为and得到的是一个交集，而&使用的是位与运算
    return bools
bool_num = sigema(res.loc[:,'amounts'])
detail = res.loc[bool_num,:]
print(detail.shape)
# 只要符合这个条件的留下，不符合这个条件的，走
"""
res = pd.read_excel('./meal_order_detail.xlsx',sheetname=0)
print(res.shape)
def sigema(data):
    bl1 = (data.mean()-3*data.std()) <=data
    bl2 = (data.mean()+3*data.std()) >=data
    bools = bl1 & bl2
    # 之所以用&而不是and，是因为and得到的是一个交集，而&使用的是位与运算
    return bools
bool_num = sigema(res.loc[:,'amounts'])
detail = res.loc[bool_num,:]
print(detail.shape)
# 只要符合这个条件的留下，不符合这个条件的，走

# 箱线图法
res = pd.read_excel('./meal_order_detail.xlsx',sheetname=0)
print(res.shape)
def box_fa(data):
    # 求出数学定义的上线与下限
    qu = data.quantile(0.75)
    ql = data.quantile(0.25)
    iqr = qu - ql

    up = qu+1.5*iqr#上限
    low = ql-1.5*iqr#下限

    bool_1 = data <= up
    bool_2 = data >= low
    bool_tj = bool_1 & bool_2

    return bool_tj

num = box_fa(res.loc[:,'amounts'])

a = res.loc[num,:]
print(a.shape)
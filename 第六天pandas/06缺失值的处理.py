# 数据清洗
import pandas as pd
import numpy as np
data = pd.read_excel('./qs.xlsx')
print(data)
print(data.dtypes)
print('='*80)

# 缺失值检测
"""
# 判断是否有缺失值
# isnull缺失值，返回T
print(data.isnull())
print(data.isnull().sum())
print('='*80)

# notnull缺失值，返回F
print(data.notnull())
print(data.notnull().sum())
print('='*80)
"""
# 判断是否有缺失值
# isnull缺失值，返回T
print(data.isnull())
print(data.isnull().sum())
print('='*80)

# notnull缺失值，返回F
print(data.notnull())
print(data.notnull().sum())
print('='*80)
# 方式1，直接删除dropna，只要有空的就删掉，按照行或者列
# any只要你这一行有空值，那么就删这行
# data.dropna(axis=0,how='any',inplace=True)
# any只要你这一列有空值，就删除
# data.dropna(axis=1,how='any',inplace=True)

# all只有整列或者整行都是缺失值，才会删除
#all对于行没什么用处
# data.dropna(axis=0,how='all',inplace=True)
# all对于列，也没用
# data.dropna(axis=1,how='all',inplace=True)
# print(data)
""""""
# 方式2 填充方法replace
#填充分为两种，
# 1 对于数值型的数据进行填充 -使用均值，中位数，众数填充
# 2 对于类别型的数据，使用众数进行填充
mode = data.loc[:,'商品ID'].mode()[0] #众数 使不使用下标都可以
print(mode)
# 使用众数进行填充
data.loc[:,'商品ID'].fillna(value=mode,inplace=True)
data.loc[:,'类别ID'].fillna(value=data.loc[:,'类别ID'].mode()[0],inplace=True)


# 对于不是NAN的数值，就不可以使用fillna的方式了
# 首先先把不是NAN的数值转化成NAN，然后再使用fillna将NAN进行填充
data.replace(to_replace='*',value=np.nan,inplace=True)
print(data)
print('='*80)



# 方式3，插值法
x = np.array([1,2,3,4,5,8,9])
y = np.array([3,5,7,9,11,17,19])#2x+1
z = np.array([2,8,18,32,50,128,162])
# 线性插值
from scipy.interpolate import interp1d
line1 = interp1d(x,y,kind='linear')
line2 = interp1d(x,z,kind='linear')
print(line1([6,7]))
print(line2([6,7]))

# 多项式插值
# 牛顿插值法、拉格朗日插值
from scipy.interpolate import lagrange#拉格朗日
la1 = lagrange(x,y)
la2 = lagrange(x,z)
print(la1([6,7]))
print(la2([6,7]))

# 样条插值,模拟曲线关系进行插值，比较准确
from  scipy.interpolate import spline
sp1 = spline(xk=x,yk=y,xnew=np.array([6,7]))
sp2 = spline(xk=x,yk=z,xnew=np.array([6,7]))
print(sp1)
print(sp2)

# 线性数据采用线性插值方式
# 非线性数据，采用多项式插值与样条插值方式
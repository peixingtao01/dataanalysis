import pandas as pd

#
detail = pd.read_excel('./concat数据拼接.xlsx',sheetname=0)
detai2 = pd.read_excel('./concat数据拼接.xlsx',sheetname=1)
print(detail)
print(detai2)
print('*'*80)
# concat拼接,必须使用元组进行拼接，而且这个可以拼接>=2的元素，所以可以一次拼接好多好多
# 行拼接 外连接，行拼接，列求并集
concat_0_o = pd.concat((detail,detai2),axis=0,join='outer')
# 行拼接，内连接，行拼接，列求交集
concat_0_i = pd.concat((detail,detai2),axis=0,join='inner')

# 列拼接，外连接，列拼接，行求并集
concat_1_o = pd.concat((detail,detai2),axis=1,join='outer')
# 列拼接，内连接，列拼接，行求交集
concat_1_i = pd.concat((detail,detai2),axis=1,join='inner')

# 这个没有左连接右连接
print(concat_0_o)
print('-'*80)
print(concat_0_i)
print('-'*80)
print(concat_1_o)
print('-'*80)
print(concat_1_i)
print('='*80)

"""

"""

# 以键连接(主键连接)
# 外连接，key值是列，求并集，没有值的使用NAN代替
# 内连接，key值是列，求交集，没有值的删除
# 左外连接，也是求并集，以左表为主，左表的行都弄完了就结束了
# 右外连接，也是求并集，以右表为主，右表的行都弄完了就结束了

# 外连接
a1 = pd.merge(left=detail,right=detai2,how='outer',on='D')
a2 = pd.merge(left=detail,right=detai2,how='outer',on=['B','D'])
# 也就是说，设置合并连接时的键可以设置两个相同的行名称
print(a1)
print('-'*80)
print(a2)
print('-'*80)

# 内连接
b1 = pd.merge(left=detail,right=detai2,how='inner',on='D')
print(b1)
print('-'*80)

# 右连接
b2 = pd.merge(left=detail,right=detai2,how='right',on='D')
print(b2)
print('-'*80)

# 左连接
b3 = pd.merge(left=detail,right=detai2,how='left',on='D')
print(b3)
print('-'*80)

# 还有一种特殊情况
# 就是两列的名称不一样，但是两列的数据一样，原来是on一个一样的，
# 现在是分别on一个
#

print(pd.merge(left=detail,right=detai2,how='outer',left_on='A',right_on='G'))
print(pd.merge(left=detail,right=detai2,how='inner',left_on='A',right_on='G'))
print(pd.merge(left=detail,right=detai2,how='left',left_on='A',right_on='G'))
print(pd.merge(left=detail,right=detai2,how='right',left_on='A',right_on='G'))

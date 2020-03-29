import pandas as pd


# 就是在表中对数据进行切片
res = pd.read_excel('meal_order_detail.xlsx')
print(res.shape)
print(res)

# 三种 直接切片  loc/iloc  ix
# 直接切片 先取列，后取行，并非同时索引
# loc/iloc 同时索引 --loc[行名称,列名称]   --iloc[行下标,列下标]
# ix 混合索引


# 直接切片，先切列，这个取出来是一个二维的
name1 = res['dishes_name'][1:10]
# name2 = res['dishes_name']['1','2','3']  不可以用字符串取数值，因为他是数值
# name2 = res['dishes_name','dishes_id'][1:6]一次想取两列的时候必须设置在一个列表中
name2 = res[['dishes_name','dishes_id']][1:6]
namex = res[['dishes_name','dishes_id']][-1:-6]#还可以取出倒数的
name3 = res[['dishes_name','dishes_id']].head()#head默认取前五个
name4 = res[['dishes_name','dishes_id']].head(11)#设置参数后可以取多个
# print(name1)
# print(name2)
# print(name3)
# print(name4)
name6 = res[['dishes_name','dishes_id']].tail()#取出倒数五个
name7 = res[['dishes_name','dishes_id']].tail(10)#取出倒数10个
# print(name6)
# print(name7)



# 使用loc/iloc -同时索引
# loc 名称 --先取行，后取列
loc_name1 = res.loc[0:10,'dishes_name']
loc_name2 = res.loc[0:10,'dishes_name':'cost':2]#设置取列的范围
loc_name3 = res.loc[[1,2,4],['dishes_name','cost']]#设置指定取某些列
# print(loc_name1)
# print(loc_name2)

# iloc 索引取值,先取行，后取列
iloc_name1 = res.iloc[0:5,0]
iloc_name2 = res.iloc[0:5,0:6:2]
iloc_name3 = res.iloc[[1,2,3],[4,5,6]]
# print(iloc_name1,'\n','*'*80)
# print(iloc_name2,'\n','*'*80)
# print(iloc_name3,'\n','*'*80)


# ix --混合索引，但是ix慢，这个也是二维的
# 也就是前面可以使用名称，后面使用下标
# 或者前面使用下标，后面使用名称
ix_name1 = res.ix[[1,2,3],[4,5,6]]
print(ix_name1,'\n','*'*80)
# 但是你只能在行或者列上用一个，比如0:10  但是不可以0:"张三"
ix_name2 = res.ix[[4,5,6],'dishes_name':'cost':2]
print(ix_name2,'\n','*'*80)
ix_name3 = res.ix[[4,5,6],['dishes_name','cost']]
print(ix_name3)
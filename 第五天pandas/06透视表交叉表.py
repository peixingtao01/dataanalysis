import pandas as pd
# 透视表就是一个列嵌套列的表
res = pd.read_excel("./meal_order_detail.xlsx")
# print(res)
res.loc[:,'place_order_time'] = pd.to_datetime(res.loc[:,'place_order_time'])
res.loc[:,'day'] =[i.day for i in res.loc[:,'place_order_time']]
day = res.loc[:,"day"]
# print(res)


# 透视表 分层索引
# x = pd.pivot_table(data=res['day'],values='amounts',columns=['day','count'],index=['order_id'],aggfunc='mean',margins=True)
# columns=['大计数分组','小计数分组']列分组
# index=['大计数分组行','小计数分组']行分组
# data 表中的数据，这个需要包含所有的数据，是所有行分组、列分组需要的数据，所以一般四个的行列需要五个数据
# aggfunc 这个是对统计的这个不在行列分组，但是在data中的哪个数据进行什么操作，比如求均值，比如计数，比如求最大值
# margins是在最后加一个总计求和，针对每一列的默认名字叫all，但是可以给它改名
x = pd.pivot_table(data=res[['amounts','order_id','counts','dishes_name','day']],values='amounts',columns=['day','counts'],index=['order_id','dishes_name'],aggfunc='mean',margins=True)
# print(x)
# x.to_excel('透视表.xlsx')


# 交叉表
# 交叉表就是制定原来表中的两列，一个作为行，一个作为列，然后显示成一个二维表的过程
# index 指定行索引，并且进行了统计
# columns 指定列索引，在行分完组的基础上，对列进行统计出现的个数
# values 指定中间要求的东西，这里是找的价格
# aggfunc是对中间要求的数据进行操作
t = pd.crosstab(index=res['order_id'],columns=res['counts'],values=res['amounts'],aggfunc='mean')
print(t)
# t.to_excel('交叉表.xlsx')
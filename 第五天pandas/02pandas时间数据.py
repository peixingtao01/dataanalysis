import pandas as pd
# numpy使用的是datetime64 的时间点类型
d = pd.to_datetime(['2016-01-01','20170101','2018.01.01','2019/01/01'])
print(d)
for i in d:
    print(i)
# 这个与to_datetime一样
x= pd.DatetimeIndex(['2016-01-01','20170101','2018.01.01','2019/01/01'])
print(x)
print("="*80)

res = pd.read_excel('./meal_order_detail.xlsx')
times = res.loc[:,'place_order_time']
nowtime =res.loc[:,'place_order_time'] = pd.to_datetime(times)

print([i.year for i in nowtime],'\n年')#获取时间数据的年
print([i.month for i in nowtime],'\n月')#获取时间数据的月
print([i.day for i in nowtime],'\n日')#获取时间数据的日
print([i.hour for i in nowtime],'\n时')#获取时间数据的时
print([i.minute for i in nowtime],'\n分')#获取时间数据的分
print([i.second for i in nowtime],'\n秒')#获取时间数据的秒

print([i.quarter for i in nowtime],'\n季度')#获取时间数据的季度
print([i.weekday_name for i in nowtime],'\n周几')#获取时间数据的周几，返回的是英文
print(len([i.weekday_name for i in nowtime]))
print([i.weekday for i in nowtime],'\n周几')#获取时间数据的周几的一个对象
print(len([i.weekday for i in nowtime]))
print("="*80)


# 时间差距计算
# howday = pd.to_datetime('2019.9.12')-pd.to_datetime('1997.11.21')
howday = pd.to_datetime('2019.9.12').year-pd.to_datetime('1997.11.21').year
print(howday)
print("="*80)

# 获取本机可以使用的最初时间与最后使用的时间节点
print(pd.Timestamp.min)
print(pd.Timestamp.max)

import pandas as pd
res = pd.read_excel('./meal_order_detail.xlsx')
# 所谓的统计分析，实际上就是分组，只不过内有内置的方法罢了
name = res.loc[:,'dishes_name'].count()
amounts = res.loc[:,'amounts']
print('amounts最大值\n',amounts.max())
print('amounts最大值位置\n',amounts.idxmax())
print('amounts最小值\n',amounts.min())
print('amounts最小值位置\n',amounts.idxmin())
print('amounts平均值\n',amounts.mean())
print('amounts中位数\n',amounts.median())
print('amounts众数\n',amounts.mode())
print('amounts方差\n',amounts.var())
print('amounts标准差\n',amounts.std())
print('amounts极差\n',amounts.ptp())
print('amounts非空值个数\n',amounts.count())#就是总数进行了过滤
print('amounts的描述\n',amounts.describe())
# describe中有计数count，平均值mean，标准差std，四分之一位数，中位数，四分之三位数，最大值

print('='*100)
# 强制类型转换
# object，强制转化成字符串数据
res.loc[:,"amounts"] = res.loc[:,"amounts"].astype('object')
print(res.loc[:,"amounts"].describe())
print('='*100)

# category类别，强制转化成类别型数据,数据之间的关联性不强
res.loc[:,"amounts"] = res.loc[:,"amounts"].astype('category')
print(res.loc[:,"amounts"].describe())
print('='*100)


# 统计出了大米白饭以外那个菜卖的最好，卖了多少
res.loc[:,"dishes_name"] = res.loc[:,'dishes_name'].astype('category')
print(res.loc[:,'dishes_name'].describe())
bool_ids = res.loc[:,'dishes_name'] == '白饭/大碗'
index = res.loc[bool_ids,:].index
res.drop(labels=index,axis=0,inplace=True)
res.loc[:,'dishes_name'] = res.loc[:,'dishes_name'].astype('category')
print(res.loc[:, 'dishes_name'].describe())

import pandas as pd

res = pd.read_excel('./users.xlsx',sheetname=0)
# print(res)

# 使用布尔数组进行查询
name_list = res.loc[:,'NAME'] =='zad'
print(name_list)
# 使用查询过滤的时候，必须使用一个等长的来过滤，否则报错
# people = res.loc[name_list,['NAME',"sex"]]
people = res.loc[name_list,:]#这样都可以显示出来
print(people)


# 现在要更改这一条数据
res.loc[name_list,'NAME']='woooooooooo'
print(res)

# 现在想修改多条数据
bool_age = res.loc[:,'age'] % 2 !=0 # 这个是这一列的每一个元素去操作
res.loc[bool_age,'age'] = res.loc[:,'age']+100
print(res)
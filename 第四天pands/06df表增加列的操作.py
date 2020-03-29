import pandas as pd

res = pd.read_excel('./users.xlsx',sheetname=0)
print(res)
# 这样是给这个表增加一列，有的话就修改这列，没有的话就创建
res.loc[:,'hahahaha']=res.loc[:,'age']+23333
print(res)
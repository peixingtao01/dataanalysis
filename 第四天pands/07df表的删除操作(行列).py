import pandas as pd

res = pd.read_excel('./users.xlsx')

# 需要指定删除的行列名称,labels
# 需要说明删除的是行还是列，axis=0 行 | =1 列
# 需要说明是否删除，inplace=True 是确认删除但是不显示，=flase是不删除，但是能让你看到删除后的效果
# res.drop(labels=['sex','age'],axis=1,inplace=True)



# 删除行
labels = res.loc[:,'age'] % 2 !=0
id = res.loc[labels,:].index
res.drop(labels=id,axis=0,inplace=True)
print(res.shape)
print(res)
# print(res)
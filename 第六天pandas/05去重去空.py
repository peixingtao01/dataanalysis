import pandas as pd
detail = pd.read_excel('./meal_order_detail.xlsx',sheetname=0)
print(detail.shape)
# 获得所有行
columns = detail.columns
drop_list = []
for column in columns:
    #drop_duplicates删除列中重复的数据，就是相当于分组一下吧
    res = detail.drop_duplicates(subset=column,inplace=False)
    if res.shape[0]==1:
        drop_list.append(column)
detail.drop(labels=drop_list,axis=1,inplace=True)
print(detail)
print(detail.shape)
import pandas as pd
res = pd.read_excel('./meal_order_detail.xlsx')
# print(res)
print(res.columns)
# place_order_time
amounts = res.loc[:,'amounts']
counts = res.loc[:,'counts']
res.loc[:,'xxx'] = amounts*counts
print(counts)
print(amounts)
print('*'*100)


res.loc[:,'day'] =[i.day for i in  res.loc[:,'place_order_time']]
print(res)
c = res.groupby(by='day')['xxx'].count()
print(c)


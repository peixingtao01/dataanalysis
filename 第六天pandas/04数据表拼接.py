import pandas as pd

# 连接多个数据表
biao1 = pd.read_excel('./meal_order_detail.xlsx',sheetname=0)
biao2 = pd.read_excel('./meal_order_detail.xlsx',sheetname=1)
biao3 = pd.read_excel('./meal_order_detail.xlsx',sheetname=2)

# 先进行内连接，求一个交集
detail = pd.concat((biao1,biao2,biao3),axis=0,join='inner')
print(detail)
print('='*80)
# 预测那些人经常点菜,点什么菜
info = pd.read_csv('./meal_order_info.csv',encoding='ansi')
print(info)
# 在内连接的基础上将两列进行合并，然后形成一个新的表
# 这个是合并了菜品id与订单id，这样就对应起来了谁点了多少菜
res1 = pd.merge(left=detail,right=info,how='inner',left_on='order_id',right_on='info_id')


users = pd.read_excel('./users.xlsx')
# 然后将这订单与名字对应起来，形成了一个名称与菜名的对应
res = pd.merge(left=res1,right=users,how='inner',left_on='name',right_on='ACCOUNT')
print(res)
res.to_excel('进行预测.xlsx')
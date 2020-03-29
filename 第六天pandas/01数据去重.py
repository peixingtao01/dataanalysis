import pandas as pd

# 对数据进行去重
detail = pd.read_excel('./meal_order_detail.xlsx')
# print(detail)
# drop_duplicates去重
print(detail.shape)
res = detail.drop_duplicates(subset='dishes_name',inplace=False)
print(res.shape)
print('='*80)
# 相关性的衡量 corr()
# 这是一个相关系数的衡量
# 默认的是皮尔逊相关系数pearson
# 还有kendall
# 还有spearman
a1 = detail.loc[:,['counts']].corr()
a2 = detail.loc[:,['amounts','counts']].corr(method='spearman')
a3 = detail.loc[:,['amounts','counts']].corr()
print(a1)
print(a2)
print(a3)

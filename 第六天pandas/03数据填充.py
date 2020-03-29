import pandas as pd

# 所谓的数据填充就是通过表2去填充表1
# 但是这两张表要起码列要相似，然后数据成分基本相同

quan = pd.read_excel('./concat数据拼接.xlsx',sheetname=1)
que = pd.read_excel('./concat数据拼接.xlsx',sheetname=2)

# 用全的表补充不全的表，形成新表
res = que.combine_first(quan)
print(res)
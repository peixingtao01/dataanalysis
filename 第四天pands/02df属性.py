import pandas as pd

# 创建一个df,这个不叫数组，这个叫表
#
df = pd.DataFrame({
    'col1':[0,1,2],
    'col2':['zs','ls','ww'],
    'col3':[3.14,2.71,1.72]
    },
    index=['一','二','三']
    )
# 用dataframe生成的东西不是数组，是增加了很多零碎的表
print(df)

# 查看dataframe 属性
print("df 的values:\n",df.values) # 获取df的数组
print("df 的values的类型:\n",type(df.values))
print("df 的index:\n",df.index) # 获取行索引名称
print("df 的columns:\n",df.columns) # 获取列索引名称
print("df 的size:\n",df.size) #  获取元素个数
# print("df 的itemsize:\n",df.itemsize) # df 没有这个属性
print("df 的dtypes:\n",df.dtypes) #  每一列的数据类型
print("df 的shape:\n",df.shape) # 获取df形状，以元组显示
print("df 的ndim:\n",df.ndim) # 获取df维度----df  是2维的 没有别的维度


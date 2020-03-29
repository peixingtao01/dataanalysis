import numpy as np
import pandas as pd
# pandas 包含数据处理，统计分析，封装了numpy
# pandas有三种结构
# series  一维结构
# dataframe 二维结构,一般都是在二维的里面取一维的
# pannel 三维结构

res = np.load('./国民经济核算季度数据.npz')
columns = res['columns']
values = res['values']

# 数组拼接 (16,)  (63,16) 行扩展
# pj = np.concatenate(([columns],values),axis=0)



# 指定列索引，columns,就是每一列的标题
# 指定行索引，index
# 这个可以将两个不同维度的数组组合起来
index = ['行'+str(i) for i in range(1,70)]
df = pd.DataFrame(values,columns=columns,index=index)
print(df)
series_s = df['时间']#即便是返回，也是加了行索引的返回
print(series_s)

# 可以自己生成一个series，但是你如果用二维的DataFrame的话，
# 会设置上标题，这有一列有文字，这个与下面的数据格式不一致
series_a=values[:,4]
S_index = ['一维'+str(i) for i in range(1,70)]
se = pd.Series(series_a,index=S_index)
print(se)
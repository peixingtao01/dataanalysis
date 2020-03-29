import matplotlib.pyplot as plt
import numpy as np

res = np.load('./国民经济核算季度数据.npz')
columns = res['columns']
values = res['values']

# 1
plt.figure()
# 默认不支持中文，需要配置RC 参数
plt.rcParams['font.sans-serif']='SimHei'
# 设置字体之后不支持负号，需要去设置RC参数更改编码
plt.rcParams['axes.unicode_minus']=False

# 2
x = np.arange(1,4)
y = values[0,3:6]

plt.bar(x,y,width=0.2,color=['r','k','c'])
# width是代表类别之间的单位间距的百分之多少
# color，可以设置成一个颜色，也可以设置成一组颜色，对应索引设置颜色

plt.title('2000年国民经济产业分布')
plt.ylabel('2000年国民经济产业分布')
plt.xticks(x,['第一产业','第二产业','第三产业'])

for i,j in zip(x,y):
    plt.text(i,j,'%.2f亿元'%j,horizontalalignment='center')

# 3
plt.show()

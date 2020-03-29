import matplotlib.pyplot as plt
import numpy as np
res = np.load('./国民经济核算季度数据.npz')
columns = res['columns']
values = res['values']

# 1
fig = plt.figure(figsize=(20,10))
#默认不支持中文，需要配置RC参数
plt.rcParams['font.sans-serif']='SimHei'#但是这个不支持负号了
# 设置字体之后，需要支持一下负号
plt.rcParams['axes.unicode_minus']=False

# 2
x = (values[:,3],values[:,4],values[:,5])
labels = [i[:4] for i in columns[3:6]]

plt.boxplot(x,notch=True,meanline=True,showmeans=True,labels=labels,vert=False,sym='D')
# notch 设置缺口
# meanline 设置中间线
# showmeans 设置中间线显示
# labels 设置替换x轴

# plt.grid(True)
# 没有设置成功网格线

# 3
plt.show()
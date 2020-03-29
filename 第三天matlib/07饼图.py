import matplotlib.pyplot as plt
import numpy as np

res = np.load('./国民经济核算季度数据.npz')
columns = res['columns']
values = res['values']



# 1
plt.figure()
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
plt.title('2000年国民经济产业分布')

# 2
a = values[1,3:6]#这个饼的分布
exploade = (0.05,0.01,0.01) #每个披萨的离心距离
labels = [i[:4] for i in columns[3:6]] #每个数据对应的名称
color = ['c','r','b']#每个披萨的颜色
atuopct = '%.1f%%'#每个披萨的数据
plt.pie(a,explode=exploade,labels=labels,colors=color,autopct=atuopct)
# 将椭圆形的饼转化成圆形的饼
plt.axis('equal')

# 3
plt.show()
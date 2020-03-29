import matplotlib.pyplot as plt
import numpy as np

res = np.load('./国民经济核算季度数据.npz')

# print(res)
# for i in res:
#     print(i)
columns = res['columns']
values = res['values']

fig =plt.figure()
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
x=[1,2,3]
t=[i[:4] for i in columns[3:6]]
# print(x)
v2000=values[0,3:6]
v2017=values[-1,3:6]
y=np.arange(9)
h2000=values[0,6:]
h2017=values[-1,6:]
s=[i[:2] for i in columns[6:]]

# fig.add_subplot(2,2,1)
# plt.bar(x,v2000)
# plt.xticks(x,t[:4],rotation=30,horizontalalignment='right',fontsize=6)
# plt.title('2000年第一季度国民生产总值产业构成分布直方图',fontsize=6)
# fig.add_subplot(2,2,2)
# plt.bar(x,v2017)
# plt.xticks(x,t[:4],rotation=30,horizontalalignment='right',fontsize=6)
# plt.title('2017年第一季度国民生产总值产业构成分布直方图',fontsize=6)
#
# fig.add_subplot(2,2,3)
# plt.bar(y,h2000)
# plt.xticks(y,s,rotation=30,horizontalalignment='right',fontsize=6)
# plt.title('2000年第一季度国民生产总值行业构成分布直方图',fontsize=6)
# fig.add_subplot(2,2,4)
# plt.bar(y,h2017)
# plt.xticks(y,s,rotation=30,horizontalalignment='right',fontsize=6)
# plt.title('2000年第一季度国民生产总值行业构成分布直方图',fontsize=6)
# plt.show()
atuopct = '%.1f%%'
fig.add_subplot(2,2,1)
plt.pie(v2000,labels=t,autopct=atuopct,textprops={"fontsize":8})
plt.axis('equal')
plt.title('2000年第一季度国民生产总值产业构成分布饼图',fontsize=10)

fig.add_subplot(2,2,2)
plt.pie(v2017,labels=t,autopct=atuopct,textprops={"fontsize":8})
plt.axis('equal')
plt.title('2017年第一季度国民生产总值产业构成分布饼图',fontsize=10)

fig.add_subplot(2,2,3)
plt.pie(h2000 ,labels=s,autopct=atuopct,textprops={"fontsize":8})
plt.axis('equal')
plt.title('2000年第一季度国民生产总值行业构成分布饼图',fontsize=10)

fig.add_subplot(2,2,4)
plt.pie(h2017 ,labels=s,autopct=atuopct,textprops={"fontsize":8})
plt.axis('equal')
plt.title('2017年第一季度国民生产总值行业构成分布饼图',fontsize=10)

plt.show()
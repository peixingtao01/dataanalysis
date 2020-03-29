import matplotlib.pyplot as plt
import numpy as np

res = np.load('./国民经济核算季度数据.npz')

# print(res)
# for i in res:
#     print(i)
columns = res['columns']
values = res['values']

print(columns)
# print(values)

# 1
fig = plt.figure(figsize=(20,10))
#默认不支持中文，需要配置RC参数
plt.rcParams['font.sans-serif']='SimHei'#但是这个不支持负号了
# 设置字体之后，需要支持一下负号
plt.rcParams['axes.unicode_minus']=False

# 2
# 创建多个多个图
fig.add_subplot(2,1,1)
x = values[:,0]
y1 = values[:,3]
y2 = values[:,4]
y3 = values[:,5]
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.title('2000-2017年各个产业与行业生产总值折线图')
plt.ylabel('生产总值(亿元)')

# 增加线条说明
legend = [i[:4] for i in columns[3:6]]
plt.legend(legend,loc=2)#线条说明
yc = plt.gca()#获得坐标轴对象
yc.spines['top'].set_color('none')#隐藏上面的线
yc.spines['right'].set_color('none')#隐藏右边的线



# 第二章图
fig.add_subplot(2,1,2)
# 参数1 小图的行数
# 参数2 小图的列数
# 参数3 第几个小图
jd = values[:,0]
print(jd)
j = values[:,1]
print(j)
# print(jd)
ny = values[:,6]
print(ny)
gy1 = values[:,7]
jz1 = values[:,8]
pf1 = values[:,9]
jt1 = values[:,10]
zs1 = values[:,11]
jr1 = values[:,12]
fd1 = values[:,13]
qt1 = values[:,14]

plt.plot(jd,ny,color='r',linestyle=':',linewidth=1.2 ,marker='D',markersize=7 ,markerfacecolor='b',markeredgecolor='m')
plt.plot(jd,gy1,color='k',linestyle=':',linewidth=1.2 ,marker='o',markersize=7 ,markerfacecolor='r',markeredgecolor='g')
plt.plot(jd,jz1,color='m',linestyle=':',linewidth=1.2 ,marker='*',markersize=7 ,markerfacecolor='k',markeredgecolor='g')
# plt.plot(jd,pf1)
# plt.plot(jd,jt1)
# plt.plot(jd,zs1)
# plt.plot(jd,jr1)
# plt.plot(jd,fd1)
# plt.plot(jd,qt1)
xticks = np.array(j)
plt.xticks(jd[::4],xticks,rotation=45,horizontalalignment='right',fontsize=6)#设置中文刻度的时候，需要设置为替换
# rotation是设置的旋转角度
legend = [i[:4] for i in columns[6:]]
plt.legend(legend,loc=2,facecolor='red', edgecolor='blue',fontsize=8)#线条说明

# # 3
plt.show()
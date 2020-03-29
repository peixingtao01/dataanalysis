import matplotlib.pyplot as plt
import numpy as np

# 1、创建画布
# plt.figure(figsize=(20,8),dpi=80)#可以设置一些参数，比如画布大小英寸，流畅度等等
hb = plt.figure()
#默认不支持中文，需要配置RC参数
plt.rcParams['font.sans-serif']='SimHei'#但是这个不支持负号了
# 设置字体之后，需要支持一下负号
plt.rcParams['axes.unicode_minus']=False

# 2、创建图片
x = np.arange(0,2*np.pi,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
# y3 = np.tan(x)
# plt.plot(x,y1)
# plt.plot(x,y2)
# plt.plot(x,y3)

# 所有的修饰放在绘图之后
# 增加标题
plt.title('sin(x)/cos(x) 曲线')

# 添加横坐标标题
plt.xlabel('x轴')
plt.ylabel('y轴',rotation=0)
# rotation改变文字方向

# 设置线条说明,需要按照程序顺序一一对应
plt.legend(['y=sinx','y=cosx'],loc=4)
# loc=1，可以放在右上角

# 设置横纵坐标刻度
xticks = np.arange(1,8)
yticks = np.arange(-1,1.1,0.5)#对于y轴的刻度只能重新创建数组
plt.yticks(yticks)
# plt.xticks(),对于x轴，如果是值，必须设置注意范围，需要考虑定义域
plt.xticks(xticks)#设置中文刻度的时候，需要设置为替换

# 设置原点

# yc = hb.add_subplot(111)#
yc = plt.gca()#获得坐标轴对象
yc.spines['top'].set_color('none')#隐藏上面的线
yc.spines['right'].set_color('none')#隐藏右边的线

# 移动轴线,先找到这个线，再设置这个线的位置
yc.xaxis.set_ticks_position('bottom')
yc.spines['bottom'].set_position(('data',0))

yc.yaxis.set_ticks_position('left')
yc.spines['left'].set_position(('data',0))


# 设置绘图点的样式
plt.plot(x,y1,color='r',linestyle=':',linewidth=1.2 ,marker='D',markersize=7 ,markerfacecolor='b',markeredgecolor='g')
plt.plot(x,y2)
# 绘图
# color 线的颜色
# linestyle  线性
# linewidth 线宽
# marker  点的形状
# markersize  点的大小
# markerfacecolor 点的填充颜色
# markeredgecolor 点的边缘颜色




# 保存图片
plt.savefig('./sin(x)cos(x)曲线.png')


# 3、图片显示
plt.show()
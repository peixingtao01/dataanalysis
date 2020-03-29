import matplotlib.pyplot as plt
import numpy as np

# 1,创建画布
plt.figure()

# 2,绘图
x = np.arange(1,8)
y = np.array([20,24,23,26,28,30,21])
plt.plot(x,y)

# 标注数据---text
for i,j in zip(x,y):
    # 参数1  x  轴位置
    # 参数2  标注的y轴位置
    # 参数3  标注的内容
    plt.text(i,j,"%d℃"%j,horizontalalignment='center')

#替换刻度
xticks = ["周一","周二","周三","周四","周五","周六","周日"]
plt.xticks(x,xticks)

# 3,显示图片
plt.show()
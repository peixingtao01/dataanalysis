import pandas as pd
# 导入标准差
from sklearn.preprocessing import StandardScaler
# 导入K-means算法
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import random

res = pd.read_csv('./company.csv',encoding='ansi')
print(res)

# 1、首先判空，处理，再聚类
res_isnull = res.isnull().sum()#得出没空

# 2、聚类
# 筛选特征值
data = res.iloc[:,:2]

def box_jc(data):
    qu = data.quantile(0.75)
    ql = data.quantile(0.25)
    iqr = qu - ql
    up = qu + iqr*1.5
    low = ql - iqr*1.5
    bl1= data<=up
    bl2= data>=low
    boolx = bl1&bl2
    return boolx

bool_id1 = box_jc(data.iloc[:,0])
bool_id2 = box_jc(data.iloc[:,1])

a = data.loc[bool_id1,:]
b = data.loc[bool_id2,:]

# 标准化数据，去除量纲影响
stand = StandardScaler()
x = stand.fit_transform(data)

print(x)
print('*'*80)
# 实现聚类分析
# n_clusters分几类
km = KMeans(n_clusters=3)
# 训练数据
km.fit(x)
# 预测数据
y_predict = km.predict(x)
# 获取聚类中心
center = km.cluster_centers_
print(center)


# 是一个类别一个类别的去将点描绘在一张图上
plt.figure()
color = ['r','b','k']
for i in range(x.shape[0]):
    plt.scatter(x[i,0],x[i,1],c=color[y_predict[i]])
plt.plot(center[:,0],center[:,1],'m*',markersize = 10)
plt.savefig('./超市用户消费水平.png')
plt.show()
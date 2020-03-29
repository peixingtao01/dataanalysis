import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
def box_fa(data):
    # 求出数学定义的上线与下限
    qu = data.quantile(0.75)
    ql = data.quantile(0.25)
    iqr = qu - ql

    up = qu + 1.5 * iqr  # 上限
    low = ql - 1.5 * iqr  # 下限

    bool_1 = data <= up
    bool_2 = data >= low
    bool_tj = bool_1 & bool_2

    return bool_tj

# 航空公司完整案例
air_data = pd.read_csv('./air_data.csv',encoding='ansi')
# 需要的数据，

# print(air_data.shape)
print(air_data.columns)
data = air_data.loc[:,['FFP_DATE','LOAD_TIME','LAST_TO_END','FLIGHT_COUNT','SEG_KM_SUM','avg_discount','SUM_YR_1','SUM_YR_2']]
# 去空
bl1 = data.loc[:,'SUM_YR_1'].notnull()
bl2 = data.loc[:,'SUM_YR_2'].notnull()
bls = bl1&bl2
data = data.loc[bls,:]

# 处理出数据
data.loc[:,'Ldays'] = pd.to_datetime(data.loc[:,'LOAD_TIME']) - pd.to_datetime(data.loc[:,'FFP_DATE'])
data.loc[:,'L'] = [i.days/30 for i in data.loc[:,'Ldays']]
# print(data.loc[:,'L'])
L = data.loc[:,'L']
data.loc[:,'R'] = [i/30 for i in data.loc[:,'LAST_TO_END']]
R = data.loc[:,'R']
data.loc[:,'F'] = data.loc[:,'FLIGHT_COUNT']
data.loc[:,'M'] = data.loc[:,'SEG_KM_SUM']
data.loc[:,'C'] = data.loc[:,'avg_discount']


# 过滤数据，处理价格
# SUM_YR_1,SUM_YR_2
pay1 = data.loc[:,'SUM_YR_1']>0
pay2 = data.loc[:,'SUM_YR_2']>0
zhe = data.loc[:,'avg_discount'] !=0
fei = data.loc[:,'SEG_KM_SUM']>0
tj = (pay1|pay2)&zhe&fei
data = data.loc[tj,:]
print(data)
# 剔除异常
# for i in range(len(data.columns)):
#     bpp = box_fa(data.iloc[:,i])
#     data = data.loc[bpp,:]
a = data.loc[:,['L','R','F','M','C']]
# 标准化数据，去掉量纲影响，就是去掉单位
stand = StandardScaler()
t = stand.fit_transform(a)


# 使用Kmeans
km = KMeans(n_clusters=5)
# 训练数据
km.fit(t)
# 预测数据
predict = km.predict(t)
# 获得聚类中心
center = km.cluster_centers_

# 画出雷达图
plt.figure()
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
# 设置分组角度，雷达图是将一个圆均匀等分，然后在半径上设置刻度，连接半径上的点，类似于设置了多个极坐标
fz = np.linspace(0,2*np.pi,num=5,endpoint=False)
# 将设置好的均匀等分的度数，连成一个圈
angle = np.concatenate((fz,[fz[0]]),axis=0)

# 画图,将五条闭合线画在一张图上
for i in range(5):
    # 每条数据都得形成一个闭合线
    data = np.concatenate((center[i,:],[center[i,0]]))
    # 先传入角度闭合，再传入连接数据点闭合
    plt.polar(angle,data)

labels = ['L','R','F','M','C']
plt.xticks(angle,labels)
plt.title('航空等级用户分析')
plt.legend(['客户等级A','客户等级B','客户等级C','客户等级D','客户等级E'])
plt.savefig('./航空等级用户分析.png')

plt.show()
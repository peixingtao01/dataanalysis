import pandas as pd
import numpy as np

# knn 算法就是将一些有标签的数据进行归类，然后对新还如的数据进行预测类别
#
class Knn_yl():
    def __init__(self):
        self.data = pd.read_excel('./电影分类数据.xlsx')
    def distance(self,v1,v2):
        x_y_chaju = np.power((v1-v2),2)
        juli2 = np.sum(x_y_chaju)
        gh = np.sqrt(juli2)
        return gh
    def tran(self):
        train = self.data.iloc[:,:6]
        print(train)
        # 获得训练集的特征值x，与目标值y
        train_x = train.iloc[:,:-1]
        train_y = train.iloc[:,-1]

        # 设置测试集
        test = self.data.columns[-4:]

        # 计算训练集与测试集的距离
        for i in range(train.shape[0]):
            dist = self.distance(train_x.iloc[i,2:5],test[1:])
            train.loc[i,'dist'] = dist
        # 将距离进行排序，然后得出距离相近的
        train.sort_values(by='dist',inplace=True)
        k=1
        res = train.loc[:,'电影类型'][:k].mode()[0]
        return res

x= Knn_yl()
a=x.tran()
print(a)
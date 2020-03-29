import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import classification_report#逻辑回归归类计算
from sklearn.metrics import roc_auc_score#auc指标
# 读取数据，不读行索引
data = pd.read_csv('./breast-cancer-wisconsin.data',header=None)

columns = ['Sample code number','Clump Thickness','Uniformity of Cell Size','Uniformity of Cell Shape','Marginal Adhesion',
           'Single Epithelial Cell Size','Bare Nuclei','Bland Chromatin','Normal Nucleoli','Mitoses','Class']
data.columns = columns#重新给表列名起名

# 处理业务异常值
data.replace('?',np.nan,inplace=True)

# 检测缺失值--行元素检测，有空子就删掉
data.dropna(axis=0,how='any',inplace=True)

# 获取特征值与目标值
# 逻辑回归只处理数组
feature = data.iloc[:,:-1].values
target = data.iloc[:,-1].values

# 检测数学异常值

# 切分数据
# 将数据切分为训练集与测试集
# 先特征值们，在目标值们
x_train,x_test,y_train,y_test =train_test_split(feature,target,test_size=0.3,random_state=1)

# 标准化数据
stand = StandardScaler()
x_train=stand.fit_transform(x_train)
x_test=stand.fit_transform(x_test)

rd = Ridge()
rd.fit(x_train,y_train)
predict = rd.predict(x_test)
score = rd.score(x_test,y_test)

k = rd.coef_
b = rd.intercept_
# 线性回归结束，接下来是逻辑回归




# 计算召回率,越大越好，说明模型成熟稳健
res = classification_report(y_test,predict,labels=[2,4],target_names=["良性","恶性"])
# 逻辑回归结束，计算损失.

# 如果样本不均衡，使用指标计算评价
"""
# 给测试集的目标值换一下名称
y_test = np.where(y_test>3,1,0)

# 计算AUC指标，针对的是样本的不平衡状态
auc = roc_auc_score(y_test,predict)
print(auc)
"""

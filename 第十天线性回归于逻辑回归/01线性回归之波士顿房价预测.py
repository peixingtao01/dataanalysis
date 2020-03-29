import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split#对数据进行切分
from sklearn.datasets import load_boston#波士顿数据

from sklearn.linear_model import LinearRegression#正规方程求解
from sklearn.linear_model import SGDRegressor#sgd线性回归.梯度下降法
from sklearn.linear_model import Ridge#岭回归


def  show_res(y_test,y_predict):
    """
    结果展示
    :param y_test:测试集目标值真实值
    :param y_predict: 预测值
    :return: None
    """
    # 1、画布
    plt.figure()

    # 默认不支持中文，需要配置RC 参数
    plt.rcParams['font.sans-serif'] = 'SimHei'
    # 设置字体之后不支持负号，需要去设置RC参数更改编码
    plt.rcParams['axes.unicode_minus'] = False

    # 2、绘图
    # 折线图
    x = np.arange(0,len(y_predict))

    #
    plt.plot(x,y_test,marker="*")
    plt.plot(x,y_predict,marker="o")

    # 增加标题
    plt.title("房价预测与真实值的走势")

    # 增加横轴、纵轴名称
    plt.xlabel("x轴")
    plt.ylabel("房价")

    # 图例
    plt.legend(["真实值","预测值"])

    # 保存
    plt.savefig("./房价预测与真实值的走势.png")
    # 3、展示
    plt.show()


# 读取数据，形成测试集与训练集
boston = load_boston()
data = boston['data']
target = boston['target']
feature_names = boston['feature_names']

df_boss = pd.DataFrame(data,columns=feature_names)
df_target = pd.DataFrame(target,columns=['MEDV'])
# 完成了总数据
df_data = pd.concat((df_boss,df_target),axis=1)

# random_state固定拆分数据
# test_size测试集占比总数据0.3
x_train,x_test,y_train,y_test = train_test_split(data,target,test_size=0.3,random_state=1)

# 检测缺失值，isnull
# 检测异常值，箱线图检测

# 标准化数据去除量纲
stand=StandardScaler()
x_train = stand.fit_transform(x_train)
x_test = stand.fit_transform(x_test)
# 只是转化特征值就行了

def zhenggui(x_train,x_test,y_train,y_test):
    # 方法1，正规方程求解方法,就是函数求解
    # 适用于特征值少，数据少的
    lr = LinearRegression()
    lr.fit(x_train,y_train)#训练集训练
    prdeict = lr.predict(x_test)
    score = lr.score(x_test,y_test)
    print(prdeict)
    print(score)
    # 获取权重与偏置值 k与b
    k = lr.coef_ #k
    b= lr.intercept_ #b
    return k,b
zhenggui(x_train,x_test,y_train,y_test)
def SGD(x_train,x_test,y_train,y_test):
    # 梯度下降法
    # 自我修正的线性模型,默认学习率为0.01 这个就是碗的下滑速度
    # 梯度方向，就是你朝着偏离正下滑的多少角度向碗底迂回前进的方向
    sgd = SGDRegressor()
    sgd.fit(x_train,y_train)
    predict=sgd.predict(x_test)
    score = sgd.score(x_test,y_test)
    print(predict)
    print(score)
    k=sgd.coef_
    b=sgd.intercept_

    return k,b
# SGD(x_train,x_test,y_train,y_test)
def Rid(x_train,x_test,y_train,y_test):
    re = Ridge()
    re.fit(x_train,y_train)
    predict = re.predict(x_test)
    score = re.score(x_test,y_test)
    print(predict)
    print(score)
    k = re.coef_
    b = re.intercept_

    return k,b
# Rid(x_train,x_test,y_train,y_test)

import numpy as np
import pandas as pd
import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB #朴素贝叶斯
data = pd.read_csv('./data.csv',encoding='ansi')
# print(data.columns)

# 将目标值转化为可以计算的数值类型
data.loc[data.loc[:,'评价']=='好评','评价']=0
data.loc[data.loc[:,'评价']=='差评','评价']=1
data.loc[:,'评价']=data.loc[:,'评价'].astype('int')
# print(data.dtypes)
# print(data)

# 分词
res_list = []
for i in data.loc[:,'内容 ']:
    res = jieba.cut(i,cut_all=False)
    res_s =','.join(res)
    res_list.append(res_s)


# 处理停用词
stop = ['看','了','，']
con_vec = CountVectorizer(stop_words=stop)
x = con_vec.fit_transform(res_list)
# 获取分词结果矩阵
feature = x.toarray()
#获取列名称
name = con_vec.get_feature_names()
# print(feature)
# print('name\n',name)

# 拼接分词结果矩阵与评价
new_data = np.concatenate((feature,data.loc[:,'评价'].values.reshape((-1,1))),axis=1)
print(new_data)

# 处理完成数据，
# 拿到训练集与测试集
train = new_data[:10,:]
test = new_data[10:,:]

# 训练数据
x_train = train[:,:-1]
y_train = train[:,-1]

# 测试数据
x_test = test[:,:-1]
y_test = test[:,-1]

# alpha=1,拉普拉斯平滑系数，就是为了便于计算，给分子分母同时加1，使得计算稳定
nb = MultinomialNB(alpha=1.0)
# 训练数据
nb.fit(x_train,y_train)
# 预测数据
predict = nb.predict(x_test)
# 得到预测分数,就是看看准不准，如果不准就再次设置训练集与测试集
score = nb.score(x_test,y_test)
print(score)
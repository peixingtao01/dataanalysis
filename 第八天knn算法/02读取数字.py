import numpy as np
import pandas as pd
import os
from sklearn.neighbors import KNeighborsClassifier

# 获得训练集与测试集
def get_data(strrs):
    train_list = os.listdir('./digits/%s/'%strrs)
    arr = []
    tigr = []
    for index,i in enumerate(train_list):
        with open('./digits/'+strrs+'/'+i,encoding='utf-8')as f:
            data = f.readlines()
            b = ''.join(data).replace('\n', '')
            b = list([int(i) for i in b])
            arr.append(b)
            tigr.append(int(i[0]))
    arr = np.array(arr)
    tigr = np.array(tigr).reshape((-1,1))
    ok = np.concatenate((arr,tigr),axis=1)
    haha = pd.DataFrame(ok)
    return haha


# 计算距离
def distance(v1,v2):
    a=np.power((v1-v2),2)
    b=np.sum(a)
    dist = np.sqrt(b)
    return dist

#实现knn算法
def K_nn(train,test):
    v1=train.loc[:,0:1024].values
    v2=test.loc[:,0:1024].values
    t_train = train.loc[:,1024].values
    t_test = train.loc[:,1024].values
    # 测试机结束，训练集必须结束
    print(test.shape[0])
    true_test=0
    for i in range(test.shape[0]):
        print(v2[i,:])
        for j in range(train.shape[0]):
            x = v2[i,:]
            y = v1[j,:]
            dist = distance(x,y)
            # 给每一行加一个特征值
            train.loc[j,'dist']=dist
        res = train.sort_values(by='dist')
        mode = res.iloc[:,-1][:3].mode()[0]
        print(mode)

        if mode==t_test[i]:
            true_test+=1
    score = true_test/test.shape[0]
    return score

def GF(train,test,k):
    knn_list=[]
    knn=KNeighborsClassifier(n_neighbors=k)
    # 训练数据
    knn.fit(train.loc[:,0:1024].values,train.iloc[:,-1].values)
    # 预测数据,应该是预测集的每一个数据返回的预测
    predict = knn.predict(test.loc[:,0:1024].values)
    # 给出分数
    score = knn.score(test.loc[:,0:1024],test.iloc[:,-1].values)
    return predict,score

if __name__ == '__main__':
    train = get_data('trainingDigits')
    test = get_data('testDigits')
    print(train.shape)
    print(test.shape)
    print('=' * 100)
    # score=K_nn(train,test)
    predict, score=GF(train,test,5)
    print(predict)
    print(score)


# 自己实现的knn算法比较慢，所以使用官方的



"""
def duqu():
    for x,y,z in wj:
        # print(x)#当前文件路径
        # print(y)#当前文件下的文件夹名
        # print(z)#当前文件夹下的文件
        h=len(z)
        train_name_list=[i[0] for i in z]
        print('文件名\n',train_name_list)
        for sz in train_name_list:
            with open('./digits/trainingDigits/0_0.txt')as f:
                sx= f.readlines()
                b= ''.join(sx).replace('\n','')
                b= list([int(i) for i in b])
                print(len(b))
"""


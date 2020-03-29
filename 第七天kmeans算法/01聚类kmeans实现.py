import numpy as np
import matplotlib.pyplot as plt

# 标准化
def build_data():
    a_list = []
    with open('./test.txt') as f:
        # data = f.readline()读第一行
        data = f.readlines()
        for line in data:
            line_object = line.strip().split('\t')
            a_list.append([float(line_object[0]),float(line_object[1])])
        # 将列表嵌套转化为数组
    data_arr = np.array(a_list)
    # print(data_arr)
    # 将二维数组转化为矩阵
    erjuzhen = np.mat(data_arr)
    print(erjuzhen)
    # 将二维数据转化为二维的矩阵，然后将矩阵进一步切分
    return erjuzhen

def center_init(data,k):
    # 随机找k个中值点，然后将数据进行归类
    columns_num = data.shape[1]
    index_num = data.shape[0]

    center = np.zeros(shape=(k,columns_num))
    # 然后再生成一个聚类中心组成的矩阵
    for i in range(k):
        r = int(np.random.uniform(0,index_num))
        center[i,:] = data[r,:]
    # 随机的挑四个,放入矩阵
    return center

def distance(v1,v2):
    dist = np.sqrt(np.sum(np.power((v1-v2),2)))
    # 计算点到聚类中心的距离
    return dist

def k_means_my(data,k):
    index_num = data.shape[0]
    columns_num = data.shape[1]
    center = center_init(data,k)#找四个聚类的点
    new_data = np.zeros(shape=(index_num,columns_num))
    flag = True
    while flag:
        flag = False
        for i in range(index_num):
            min_dist = 1000000
            min_index=-1
            for j in range(k):
                # 逐一计算每个点到每一个聚类中心的距离
                dist = distance(data[i,:],center[j,:])
                if dist < min_dist:
                    min_dist = dist
                    min_index = j
            if new_data[i,1] != min_index:
                flag = True
                new_data[i,:] = min_dist,min_index
                # 当聚类中心还是会变化的时候，就一直循环；如果聚类中心不变了，那么就稳定了
        for p in range(k):
            p_clustor = data[new_data[:,1]==p,:]
            center[p,:] = p_clustor[:,0].mean(),p_clustor[:,1].mean()
    #         在当前聚类中心的基础上，对所有数据进行分类，它属于什么聚类中心，就给一个标签
    return new_data,center

def show_res(data,new_data,center):
    plt.figure()
    index_num = data.shape[0]
    colors = ['r','g','m','y']
    for i  in range(index_num):
        plt.scatter(data[i,0],data[i,1],c=colors[int(new_data[i,1])])
    plt.plot(center[:,0],center[:,1],'bD',markersize=10)
    plt.show()

if __name__ == '__main__':
    data = build_data()
    k=4
    new_data,center=k_means_my(data,k)
    show_res(data,new_data,center)
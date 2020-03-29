import tensorflow as tf

class MyLinearRegression(object):
    def __init__(self):
        self.leaing_rate=0.01
    def build_data(self):
        # 构建数据，就是规定数据
        with tf.variable_scope('build_data'):
            x = tf.random_normal(shape=[100,1],mean=0.0,stddev=0.0,dtype=tf.float32)
            y = tf.matmul(x,[[0.7]])+0.8
        return x,y
    def get_weight(self):
        # 获取权重
        initial_value = tf.random_normal(shape=[1,1],mean=1.0,stddev=1.0)
        weight = tf.Variable(initial_value=initial_value,name='w')
        return weight
    def get_bias(self):
        # 设置偏置值
        initial_value = tf.random_normal(shape=[1,1],mean=1.0,stddev=1.0)
        bias  =tf.Variable(initial_value=initial_value,name='b')
        return bias
    def linear_model(self,x):
        # 构建线性模型
        with tf.variable_scope('linear_model'):
            self.weight = self.get_weight()
            self.bais = self.get_bias()
            y_predict = tf.matmul(x,self.weight)+self.bais
        return y_predict
    def loss(self,y_true,y_predict):
        # 计算军方误差
        with tf.variable_scope('loss'):
            loss = tf.reduce_mean(tf.square(y_true-y_predict))
        return loss
    def sgd(self,loss):
        # 梯度下降优化
        # minimize(loss)减小损失
        with tf.variable_scope('sgd'):
            train_op = tf.train.GradientDescentOptimizer(self.leaing_rate).minimize(loss)
        return train_op
    def train(self):
        # 训练数据
        x,y_true = self.build_data()
        # 构建线性模型
        y_predict = self.linear_model(x)
        # 计算均方误差
        loss = self.loss(y_true,y_predict)
        # 优化梯度下降算法
        train_op = self.sgd(loss)
        # 开启会话层，运行算法
        with tf.Session() as ss:
            ss.run(tf.global_variables_initializer())
            tf.summary.FileWriter('./tmp/',graph=ss.graph)
            for i in range(500):
                ss.run(train_op)
                print("第%d 次的损失为：%f ,权重为：%f,偏置为：%f" % (
                    i,
                    loss.eval(),
                    self.weight.eval(),
                    self.bais.eval())
                      )

# 实例化对象
lr = MyLinearRegression()

# 调用train方法
lr.train()
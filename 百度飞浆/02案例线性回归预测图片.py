import paddle
import paddle.batch
import paddle.fluid as fluid

# 指定训练场所
place = fluid.CPUPlace()

# 构建全连接网络
# 1、特征层
image = fluid.layers.data(name='image',shape=[1,28,28],dtype='float32')
# 2、目标层
label = fluid.layers.data(name='label',shape=[1],dtype='int32')
# 3、准备卷积层+激活函数,
fc1 = fluid.layers.fc(input=image,size=128,act='relu')
fc2 = fluid.layers.fc(input=label,size=128,act='relu')
# 4、输出层
y_prdict = fluid.layers.fc(input=fc2,size=10,act='softmax')

# 计算损失，得到准确率，进行梯度下降
# 使用预测值与真实值计算损失
loss = fluid.layers.cross_entropy(input=y_prdict,label=label)
# 计算平均损失
avg_loss = fluid.layers.mean(loss)

# 计算准确率
acc = fluid.layers.accuracy(input=y_prdict,label=label)

# 梯度下降优化
# 1、先设置学习率
sgd_optimizer = fluid.optimizer.SGDOptimizer(learning_rate=0.01)
# 2、优化损失对象
sgd_optimizer.minimize(avg_loss)

# 进行训练
# 设置映射关系
feeder = fluid.DataFeeder(feed_list=[image,label],place=place)
# 设置执行器--在执行场所设置执行器
exe_train = fluid.Executor(place=place)#训练执行器
exe_test = fluid.Executor(place=place)#测试执行器


# 申请一个程序
start_program = fluid.default_main_program()
# 设置一个主程序执行训练集
train_program = fluid.default_main_program()
# 设置一个再次主程序执行测试集
test_program = train_program.clone(for_test=True)
# 执行器中跑申请主程序
exe_train.run(start_program)

# 获取数据
# 一次读取全部数据，放入缓冲区,batch_size批量获取样本，buf_size缓冲区大小
train_reader=paddle.batch(
    paddle.reader.shuffle(
        paddle.dataset.mnist.train(),
        buf_size=200
    ),
    batch_size = 20
)

test_reader=paddle.batch(
    paddle.reader.shuffle(
        paddle.dataset.mnist.test(),
        buf_size=200
    ),
    batch_size = 20
)

# 测试函数
def train_test(Executor,program,reader,feeder,fetch_list):
    ls = [0]
    ac = [0]
    count = 0
    for data in reader():
        avg_loss_value_test,avg_loss_value=Executor.run(
            program=program,
            feed = feeder.feed(data),
            fetch_list = fetch_list
        )
        ls = [x[0]+x[1] for x in zip(ls,avg_loss_value_test)]
        ac = [x[0]+x[1] for x in zip(ac,avg_loss_value)]
        count+=1
    avg_loss_test = ls[0]/count
    avg_acc_test = ls[0]/count
    return avg_loss_test,avg_acc_test

# 执行几次神经网络
loop_num = 2
step = 0
for loop in range(loop_num):
    for data in train_reader():
        avg_loss_value_train, acc_value_train=exe_train.run(
            program=train_program,
            feed = feeder.feed(data),
            fetch_list=[avg_loss,acc]
        )
        if step%10==0:
            print('')
        if step%100==0:
            avg_loss_test,avg_acc_test=train_test(
                Executor=exe_test,
                program=test_program,
                reader=test_reader,
                feeder=feeder,
                fetch_list=[avg_loss,acc]
            )
        if avg_loss_test <= 0.2 and avg_acc_test >= 0.95:
            print("测试集平均损失为：", avg_loss_test)
            print("测试集平均准确率为：", avg_acc_test)
            break
        step+=1

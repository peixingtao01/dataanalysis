import tensorflow as tf

# 除了加法运算之外还有其他的运算操作
#
a = tf.constant(3.0,name='a')
b = tf.constant(4.0,name='b')

# op叫操作也叫指令。就好像pv操作,就是pv指令一般
# c = tf.sub()

c = tf.add(a,b)

f = tf.placeholder(dtype=tf.int32,shape=[2,2],name='f')

# 运行回话并打印设备信息
# log_device_placement=True))
# target ---指定运行远程设备
# graph ---指定需要运行的图
#  config  打印运行的相关系--包括映射关系与运行设备
sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True,log_device_placement=True))


# 创建一个形式op，作为一个矩阵
with tf.Session() as ss:
    print(ss.run(f,feed_dict={f:[[1,2],[3,4]]}))
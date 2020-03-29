import tensorflow as tf
a = tf.constant(3.0)
b = tf.constant(4.0)

c= tf.add(a,b)

with tf.Session() as ss:
    tf.summary.FileWriter('./tmp/', graph=ss.graph)
    # 序列化 ---events 文件。可视化学习创建图
    # 参数1  序列化之后的文件放置的路径
    # 参数2  就是需要序列化的参数---图

    print(ss.run(c))
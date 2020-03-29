import tensorflow as tf
import datetime
print(datetime.datetime.now().year)
print(lambda: datetime.datetime(2012, 12, 12))
def f(*args,**kwargs):
    print(args,kwargs)
f()
f(1,2,3)
# 定义一下不用cup进行加速运算
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2'



# 构建流图
con_a = tf.constant(3.0)
con_b = tf.constant(4.0)
con_c = tf.add(con_a,con_b)

# ----------------------------------------------------
# 自定义一个图
g = tf.Graph()
print(g)
# 给自定义的图进行操作
with g.as_default():
    g_a = tf.constant(8.0)
    # 这是形成一个张亮
    print(g_a)
# 开启g图
with tf.Session(graph=g) as ss:
    print(ss.run(g_a))
# ----------------------------------------------------
#



# 开启会话,打开图，看效果，
# 也就是你定义好了图之后，你怎么去操作图
with tf.Session() as sess:
    pass
    # print(sess.run(con_c))


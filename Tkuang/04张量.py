import tensorflow as tf

# 创建op，默认不进行强制转化
a = tf.constant(3.0,dtype=tf.float64)
b = tf.constant([3.0,4.0],dtype=tf.float64)
c = tf.constant([[3.0,4.0],[5.0,6.0]],dtype=tf.float64)

# 张量，其实就是与np.array的形状一样，不过是在这个框架内部得这么写
print(a.shape)
print(b.shape)
print(c.shape)
"""

"""
# 转化类型的方式之一
a = tf.to_int32(a,name='to_int32')
print(a)

# 方式2
b=tf.cast(b,dtype=tf.int32,name='cast_int32')
print(b)

c= tf.cast(c,dtype=tf.string,name='cast_str')
print(c)
# 也可以转化为字符串类型

# 创建张量
# 张亮有三种，固定值，符合正态随机，占位置张亮
# 固定值三种
m = tf.ones(shape=(2,2))
n = tf.zeros(shape=(2,2))
o = tf.constant([[1,2],[3,4]],shape=(2,2))
# 随机张亮，符合正态分布
w = tf.random_normal(shape=(2,2),mean=0.0,stddev=1.0,dtype=tf.float64)
# 占位置张亮，某个维度不确定
g = tf.placeholder(dtype=tf.float64,shape=[None,2],name='g')

# 改变形状
# reshape,动态的改变形状
x = tf.reshape(w,shape=(4,1))
y = tf.reshape(w,shape=(1,1,2,2))

# set_shape 静态的改变形状
# 只能把形状不确定的形状给确定下来，所以只使用于占位置的张亮
w.set_shape(shape=(2,2))

with tf.Session() as ss:
    print(ss.run(w))
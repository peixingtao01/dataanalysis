import tensorflow as tf
# 创建变量op,随机张量
intit_value_1 = tf.random_normal(
    dtype=tf.float64,
    shape=[2,2],
    stddev=1.0,
    mean=0.0
)

intit_value_2 = tf.random_normal(
    dtype=tf.float64,
    shape=[2,2],
    stddev=1.0,
    mean=0.0
)

# 定义相同名字的变量
var_1 = tf.Variable(initial_value=intit_value_1,name='var')
var_2 = tf.Variable(initial_value=intit_value_2,name='var')
# 给变量一个值
res = var_1.assign_add([[1.0,1.0],[1.0,1.0]])

# 初始化变量
init_op = tf.global_variables_initializer()
# with tf.Session() as ss:
#     # 所谓的显示初始化，就是运行变量
#     ss.run(init_op)
#     print(ss.run(res))
#     print(ss.run(var_1))
#     print(ss.run(var_2))

# 定义命名空间，
# 这个是可以修改命名空间的名称
with tf.variable_scope('variable',reuse=tf.AUTO_REUSE):
    inii_1 = tf.random_normal(
        dtype=tf.float64,
        shape=[2,2],
        stddev=1.0,
        mean=0.0
    )
    inii_2 = tf.random_normal(
        dtype=tf.float64,
        shape=[2,2],
        stddev=1.0,
        mean=0.0
    )
    var_11 = tf.get_variable(initializer=inii_1,name='var',dtype=tf.float64)
    var_22= tf.get_variable(initializer=inii_2,name='var',dtype=tf.float64)

with tf.Session() as ss:
    ss.run(tf.global_variables_initializer())
    print(ss.run([var_11,var_22]))
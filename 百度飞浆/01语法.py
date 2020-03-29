import paddle
import paddle.fluid as fluid

# 数据场所
place = fluid.CPUPlace()

# 数据处理

# 定义特征层，目标层
# 构建fc网络
# 定义均方误差损失
# 求误差平均值
# 使用sgd进行优化
# 朝着损失减小的方向优化
# 定义一个映射关系
# 定义执行器来执行程序
# 训练完成之后初始化数据
# 循环训练

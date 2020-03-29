import numpy as np

# sort排序，如果是一维的，那么直接就是升序排序
# 如果是多维的，在最小的维度中排序
arr1 = np.array([[2,5,3,7],[9,7,1,8]])
arr1.sort()
# print(arr1)

arr2 = np.array([2,5,3,7,9,7,1,8])
arr2.sort()
# print(arr2)

arr3 = np.array([[[1,3,2,4],[4,6,9,8],[0,2,5,1],[9,7,1,8]],[[1,3,2,4],[4,6,9,8],[0,2,5,1],[7,2,3,5]],[[0,2,5,1],[1,3,2,4],[9,7,1,8],[3,5,7,1]]])
arr3.sort()
print(arr3)
print('='*80)
# argsort将升序排序后的原来数字的索引按照排序后的位置返回
a=np.array([7,3,6,9,1])
print(np.argsort(a))


# lexsort,按照最后一个数组规则给自己排序
x=np.array([1,2,3,4,5])
y=np.array([2,5,8,10,12])
z=np.array([7,3,6,9,1])
res = np.lexsort([x,y,z])
print(res)

# 自定义排序规则
# 这样规定了一种排序方式，然后将x按照这个规则进行排序
b = [x[i] for i in res]
print(b)
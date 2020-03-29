import numpy as np

arr1 = np.arange(4).reshape(2,2)
arr2 = np.arange(4,8).reshape(2,2)
print(arr1)
print(arr2)
# 数组四则运算
# 数组的加减乘除都是符合对应元素的加减乘除，与结构无关
print('数组加\n',arr1+arr2)
print('数组减\n',arr1-arr2)
print('数组乘\n',arr1*arr2)
print('数组除\n',arr1/arr2)



# 数组的比较运算,
# 对应元素比较运算，是一一对应的，也是与结构无关
print('大于运算\n',arr1 > arr2)
print('大于等于运算\n',arr1 >= arr2)
print('小于运算\n',arr1 < arr2)
print('小于等于运算\n',arr1 <= arr2)
print('等于运算\n',arr1 == arr2)
print('不等于运算\n',arr1 != arr2)

# 逻辑运算
# 逻辑运算是判断比较运算，只要逻辑比较运算中有符合条件的 就会返回TRUE，或者false
# any代表or
print(np.any(arr1==arr2))
# all代表and
print(np.all(arr1==arr2))
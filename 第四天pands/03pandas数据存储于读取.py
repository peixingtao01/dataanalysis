import numpy as np
import pandas as pd

# read_table,需要设置分隔符号，默认使用\t分隔的,空格分隔,这个只是适用于文本形式的文件
# info  = pd.read_table('./meal_order_info.csv',encoding='ansi',sep=',')
# print(info)

# 还有read_csv方式，默认逗号分隔，
index_col = [0,1,2,3]# 将某几列的名字下沉，作为一行，不再当做列名使用了
# nrows 是读取前几行，只能是数字参数
# usecols=['info_id','name'] 读取指定的几列，这个只能用列表
# xinfo = pd.read_csv('./meal_order_info.csv',encoding='gbk',usecols=['info_id','name'])
# 你直接pycharm打开就可以看到提示的编码格式了,不用设置分隔符号,这个只能打开csv
# print(xinfo)




# meal_order_detail.xlsx
# 读取excel文件，后缀是.xlsx ,.xls结尾的文件
# header 把某一行作为列名
# names 像是read_csv的names
# parse_cols 是在某个版本中有作用
# index_col 下沉某个列名作为一行 ,index_col='dishes_name'
# usecols=['dishes_name'] 显示想要的某列名
x = pd.read_excel('meal_order_detail.xlsx',sheetname=2,usecols=['dishes_name'])
print(x)


# 保存数据
# 保存数据是以保存表的形式，所以直接是表进行操作,而不是函数
# to_csv
# to_excel
a = ['a'+str(i) for i in range(3611)]
x.to_excel('./hh.xls',index_label=a)
x.to_csv('./hh.csv')
# columns  --指定需要保存的列
# header   --保存列索引
# index    --保存行索引
# index_label -给行索引起一个名字
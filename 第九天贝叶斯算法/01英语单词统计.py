import pandas as pd
import numpy as np
import jieba
# 文本特征提取
from sklearn.feature_extraction.text import CountVectorizer

#英文的分词直接使用 CountVectorizer就很好了，因为它默认按照
content = ['我想要怒放的生命','如今我已不再感到彷徨','如今我已不再感到迷茫','曾经多少次破灭了梦想','我要我的生命得到解放']

content_list =[]
# 中文分词是使用结巴分词对每一个字符串进行分词，所以对列表无效
for i in content:
    # 结巴分词的三种模式之 精准模式分词，不在追加零碎
    res = jieba.cut(i,cut_all=False)
    print(res)#是一个字符串样式的东西，但是不显示，一个指针
    res_str = ','.join(res)
    content_list.append(res_str)
print(content_list)


# 拿到分完词语之后，使用文本特征提取，
# 设置不提取的列表stop_words
# 就是为了抛弃那种没有语言色彩，不会表达情感的词语，通过剩下的东西得到主人公的心情
con_vet = CountVectorizer(stop_words=['我','我要','多少'])

# 词语提取
x=con_vet.fit_transform(content_list)

# 提取出词语之后，需要获得这些词语
name = con_vet.get_feature_names()

print(name)

# 获得词语分布
# 得到了一个词语分布的列表，是根据每一个列表项构建的，
# 统计了这些元素在列表项出现的个数与出现的位置
print(x.toarray())
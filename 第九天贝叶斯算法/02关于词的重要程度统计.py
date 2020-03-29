from sklearn.feature_extraction.text import TfidfVectorizer
content = ['This is the first document.', 'This is the second second document.', 'And the third one.', 'Is this the first document? i x y' ]

# 设置停用词语
tf = TfidfVectorizer(stop_words=['This','is'])
# 统计分词的重要程度，这个会形成矩阵
x= tf.fit_transform(content)
# 获取分词的结果
name = tf.get_feature_names()
print(name)
print(x.toarray())
#!/usr/bin/env python
# coding: utf-8

# In[2]:


#分词
from snownlp import SnowNLP

s = SnowNLP(u"我是个没得感情的Deadline Killer。")

print(s.words)


# In[5]:


#词性标注
from snownlp import SnowNLP

s = SnowNLP(u"我是个没得感情的Deadline Killer。")

for x in s.tags:
    print(x)


# In[6]:


#情感分析
text1 = '今天作业不太多'
s1 = SnowNLP(text1)
print(s1.sentiments)

text2 = '今天作业好多'
s2 = SnowNLP(text2)
print(s2.sentiments)

text3 = '今天作业有点多'
s3 = SnowNLP(text3)
print(s3.sentiments)


# In[10]:


#转换成拼音
from snownlp import SnowNLP

s1 = SnowNLP(u"我睡得很晚")
print(s1.pinyin)

s2 = SnowNLP(u"焚膏继晷")
print(s2.pinyin)


# In[2]:


#繁体转简体
from snownlp import SnowNLP
s = SnowNLP(u'「繁體字」「繁體中文」的叫法在臺灣亦很常見。')

print(s.han)


# In[3]:


#提取文本摘要
from snownlp import SnowNLP

text = u'''
自然语言处理是计算机科学领域与人工智能领域中的一个重要方向。
它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法。
自然语言处理是一门融语言学、计算机科学、数学于一体的科学。
因此，这一领域的研究将涉及自然语言，即人们日常使用的语言，
所以它与语言学的研究有着密切的联系，但又有重要的区别。
自然语言处理并不是一般地研究自然语言，
而在于研制能有效地实现自然语言通信的计算机系统，
特别是其中的软件系统。因而它是计算机科学的一部分。
'''
s = SnowNLP(text)
print(s.summary(10))


# In[4]:


#信息量衡量
from snownlp import SnowNLP

text = [
    [u'性格', u'温柔'],
    [u'善良', u'温柔', u'美丽', u'善良'],
    [u'好人'],
    [u'善良', u'善良'],
    [u'美丽', u'性格', u'温柔']
]
s = SnowNLP(text)
print(s.tf)
print(s.idf)


# In[5]:


#文本相似
from snownlp import SnowNLP

text = [
    [u'性格', u'温柔'],
    [u'善良', u'温柔', u'美丽', u'善良'],
    [u'好人'],
    [u'善良', u'善良'],
    [u'美丽', u'性格', u'温柔']
]
s = SnowNLP(text)
print(s.sim([u'温柔']))
print(s.sim([u'好人']))


# In[ ]:





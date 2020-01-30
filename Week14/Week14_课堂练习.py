#!/usr/bin/env python
# coding: utf-8

# In[54]:


def calculation_pro(t):
    t_length = len(t)
    right_sample = ['在','尼比鲁星球','探查','期间','，','企业号','舰长','柯克','为','营救','史波克','采取','了','胆大妄为','的','举动','，','几乎','危及','全舰','队员','的','生命','，','他','也','为此','付出','代价','。']
    r_length = len(right_sample)
    j = 0
    for i in range(r_length):       
        if right_sample[i] in t:
            j = j+1
    print("切分结果中所有分词数：",t_length)
    print("标准答案中所有分词数：",r_length)
    print("切分结果中正确分词数：",j)
    p = j/t_length
    r = j/r_length
    f = 2*p*r/(p+r)
    print("准确率为：",p)
    print("召回率为：",r)
    print("F-指标为：",f)


# In[55]:


text = "在尼比鲁星球探查期间，企业号舰长柯克为营救史波克采取了胆大妄为的举动，几乎危及全舰队员的生命，他也为此付出代价。"

# snownlp
from snownlp import SnowNLP
doc = SnowNLP(text)
calculation_pro(doc.words)


# In[56]:


# jieba
import jieba
words = jieba.cut(text)
test = []
for w in words:
    test.append(w)
calculation_pro(test)


# In[ ]:





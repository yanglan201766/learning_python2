#!/usr/bin/env python
# coding: utf-8

# In[1]:


from snownlp import SnowNLP
text = "在尼比鲁星球探查期间，企业号舰长柯克为营救史波克采取了胆大妄为的举动，几乎危及全舰队员的生命，他也为此付出代价。"
s = SnowNLP(text)
print(s.words)
print([t for t in s.tags])


# In[ ]:


from stanfordcorenlp import StanfordCoreNLP
from nltk.tree import ParentedTree as PT
from nltk.treeprettyprinter import TreePrettyPrinter

corenlp = StanfordCoreNLP('http://localhost',port=2002)
text="Once again, Coca-Cola, Nestlé, and PepsiCo are the world's worst plastic pollution contributors, according to a recent global audit."
tstr = corenlp.parse(text)
pt = PT.fromstring(tstr)


# In[ ]:


dir(t2)


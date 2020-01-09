#!/usr/bin/env python
# coding: utf-8

# In[30]:


# 在浏览器中打开网址https://www.beijing2022.cn/cn/presscentre/newslist.htm 循环将网页中新闻列表的新闻标题用jquery的方法抽取出来
import requests
from pyquery import PyQuery as pq
import ssl

url = 'http://wwwnew.blcu.edu.cn/' #原来的冬奥会新闻网页是用js写的，按照老师课上的要求换成了北语的新闻网页
r = requests.get(url,verify=False)
r.encoding='utf-8'
html = r.text


# In[31]:


html


# In[32]:


doc = pq(html)


# In[33]:


doc('head').text()


# In[34]:


doc('body').text()


# In[60]:


doc = pq(html)
lis = doc('.text2')


# In[61]:


lis.text()


# In[62]:


for li in lis:
    print(pq(li).find('a').text())


# In[ ]:





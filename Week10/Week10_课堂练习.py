#!/usr/bin/env python
# coding: utf-8

# In[6]:


# 使用selenium webdriver调用chrome, 访问www.baidu.com，并用程序控制在检索框输入自己的姓名，抽取搜索结果列表的内容和分页的链接列表。
from selenium import webdriver
from pyquery import PyQuery as pq

dr = webdriver.Chrome()
dr.get('https://www.baidu.com/')
s = dr.page_source
print(s)


# In[7]:


dr.find_elements_by_id('kw')[0].send_keys('杨澜')


# In[8]:


dr.find_elements_by_id('su')[0].click()


# In[14]:


s=dr.page_source


# In[15]:


docl = pq(s)
docl('#content_left div')


# In[ ]:





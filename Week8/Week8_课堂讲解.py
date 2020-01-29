#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests


# In[3]:


url = 'https://www.beijing2022.cn/cn/presscentre/newslist.htm'


# In[4]:


from pyquery import PyQuery as pq


# In[5]:


r = requests.get(url)


# In[6]:


import ssl


# In[8]:


x = requests.get(url,verify=False)


# In[9]:


x.status


# In[11]:


x.status_code


# In[12]:


type(x)


# In[13]:


html_text = x.text


# In[14]:


html_text


# In[15]:


doc = pq(html_text)


# In[16]:


type(doc)


# In[17]:


doc('head title').text()


# In[22]:


lis = doc('#listZone a')


# In[23]:


lis[0]


# In[28]:


import requests
from pyquery import PyQuery as pq

url = 'http://wwwnew.blcu.edu.cn/'
r = requests.get(url,verify=False)
html = r.text.encoding(r.encoding)


# In[29]:


html


# In[30]:


doc = pq(html)
lis = doc('#listZone .news_dp a')


# In[31]:





# In[ ]:





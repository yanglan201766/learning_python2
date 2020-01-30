#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver
dr = webdriver.Chrome()


# In[4]:


dr.get('http://www.blcu.edu.cn')


# In[5]:


s = dr.page_source
(/获得网页源码)


# In[6]:


print(s)


# In[7]:


dir(dr)


# In[8]:


from pyquery import PyQuery as pq
doc = pq(s)


# In[9]:


doc('.zcontent').text()


# In[10]:


print(doc('.zcontent').text())


# In[11]:


lst = doc('.zcontent li')


# In[12]:


lst 


# In[14]:


pq(lst[0]).find('h2 a').text()


# In[15]:


pq(lst[0]).find('p.zc_date gray').text()


# In[16]:


pq(lst[0]).find('p.zc_date').text()


# In[17]:


dr.get('http://cn.bing.com')


# In[19]:


dr.find_elements_by_id('sb_form_q')


# In[22]:


dr.find_elements_by_id('sb_form_q')[0].send_keys('Winter')


# In[23]:


dr.find_elements_by_id('sb_form_q')[0].click


# In[24]:


s = dr.page_source


# In[25]:


print(s)


# In[26]:


docl = pq(s)
docl('#b_results li')


# In[27]:


docl = pq(s)
lst = docl('#b_results li')


# In[28]:


lst


# In[29]:


li = lst[4]


# In[31]:


pq(li).find('.b_title h2 a').text()


# In[32]:


li


# In[33]:


pq(li).find('h2 a').text()


# In[34]:


pq(li).text()


# In[35]:


dr.get('https://www.baidu.com/')


# In[36]:


s = dr.page_source


# In[37]:


print(s)


# In[48]:


dr.find_elements_by_id('kw')[0].send_keys('杨澜')


# In[49]:


dr.find_elements_by_id('su')[0].click()


# In[51]:


s=dr.page_source


# In[54]:


docl = pq(s)
docl('#content_left div')


# In[55]:


docl = pq(s)
lst = docl('#content_left div')


# In[56]:


lst


# In[ ]:


lst[]


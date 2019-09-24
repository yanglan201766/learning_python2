#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Week2 课堂练习一

j = 66
t = 98
a = [(65,97)]
print (chr(a[0][0]),"-",chr(a[0][1]))
for i in range(1,26):
    tul = (j,t)
    a.append(tul)
    print (chr(a[i][0]),"-",chr(a[i][1]))
    j += 1
    t += 1


# In[9]:


#Week2 课堂练习二
import os

path = r'E:\Learning_Python'
prefix = './test'
for i in range(1,51):
    os.mkdir(path+prefix+str(i))


# In[ ]:





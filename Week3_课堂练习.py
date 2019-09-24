#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Week3 课堂练习

def printfo(num):
    for i in range(1,num):
        for j in range(0,i):
            print (j+1,'*',i,'=',i*(j+1),end='  ')
        print ('\n')
printfo(10)


# In[ ]:





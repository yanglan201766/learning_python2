#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Week2 课后练习一

a = b = c = d = 0

for i in range(1,10001):
    if i%2 == 0:
        a = a + i
    if i%3 == 0:
        b = b + i
    if i%4 == 0:
        c = c + i
    if i%5 == 0:
        d = d + i
        
print ('10000以内2的倍数的和为：',a)
print ('10000以内3的倍数的和为：',b)
print ('10000以内4的倍数的和为：',c)
print ('10000以内5的倍数的和为：',d)


# In[11]:


#Week2 课后练习二

asci = []
k = 0

for i in range(33,128):
    asci.append(chr(i))
    
for j in asci:
    print (j,end=" ")
    k = k + 1
    if k%20 == 0:
        print('\n')
    


# In[ ]:





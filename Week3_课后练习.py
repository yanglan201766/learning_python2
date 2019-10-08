#!/usr/bin/env python
# coding: utf-8

# In[72]:


month = ['January','February','March','April','May','June','July','August','September','October','November','December']
big_month = [1,3,5,7,8,10,12]
small_month = [4,6,9,11]

def curse(m):
    if m in [1,4,7]:
        return 3
    elif m in [2,8]:
        return 6
    elif m in [3,11]:
        return 7
    elif m in [9,12]:
        return 2
    elif m == 5:
        return 5
    elif m == 6:
        return 1
    elif m == 10:
        return 4
    

for i in range(1,13):
    print ('\n'*2," "*4,month[i-1])
    print ("Mo Tu We Th Fr Sa Su")
    if i in big_month:
        print ("   "*(curse(i)-1),end="")
        for j in range(1,32):
            print (repr(j).rjust(2),"",end='')
            if (j+curse(i)-1)%7 == 0:
                print ('\n')
    elif i in small_month:
        print ("   "*(curse(i)-1),end="")
        for j in range(1,31):
            print (repr(j).rjust(2),"",end='')
            if (j+curse(i)-1)%7 == 0:
                print ('\n')
    else :
        print ("   "*(curse(i)-1),end="")
        for j in range(1,30):
            print (repr(j).rjust(2),"",end='')
            if (j+curse(i)-1)%7 == 0:
                print ('\n')
        


# In[ ]:





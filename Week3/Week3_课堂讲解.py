#!/usr/bin/env python
# coding: utf-8

# In[1]:


def printinfo( arg1, *vartuple ):
    # 打印任何传入的参数
    print ("输出")
    print (arg1)
    print (*vartuple)


# In[4]:


printinfo( 70, 60, 50 )


# In[5]:


printinfo( 70, 60, 50, 40, 30, 20, 10 )


# In[6]:


def printinfo( arg1, **vartuple ):
    # 打印任何传入的参数
    print ("输出")
    print (arg1)
    print (vartuple)


# In[7]:


printinfo(1, a=2,b=3)


# In[8]:


def ChangeInt( a ):
    a = 10

b = 2
ChangeInt(b)
print( b )


# In[9]:


# 传可变对象实例
# 可写函数说明
def changeme( mylist ):
   #"修改传入的列表"
   mylist.append([1,2,3,4])
   print ("函数内取值: ", mylist)
   return
 
# 调用changeme函数
mylist = [10,20,30]
changeme( mylist )
print ("函数外取值: ", mylist)


# In[11]:


multiply = lambda x, y: x * y
square = lambda x: x * x
# 调用sum函数
print (multiply( 2,3 ))
print ( square( 4 ))


# In[12]:


def multiply(x,y):
    return x*y


# In[13]:


def square(x):
    return x*x


# In[14]:


def multiply_and_square(x,y):
    return (x*y,x*x,y*y)


# In[15]:


ret = multiply_and_square(1,2)


# In[16]:


ret


# In[17]:


ret1, ret2, ret3 = multiply_and_square(1,2)


# In[18]:


ret1


# In[19]:


ret2


# In[20]:


ret3


# In[ ]:





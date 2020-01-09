#!/usr/bin/env python
# coding: utf-8

# In[22]:


#练习一 1.读取压缩包 books.zip中解压缩后的文本文件，以文件名为键，文件中文本的长度为值，组成一个字典
import os

filenames = []
lenlist = []

namelist = os.listdir("books") #获取指定文件夹下的文件名

for filename in namelist:
    fpath = "E:/Learning_Python/workspace/learning_python2/books/"+filename
    f = open(fpath)
    file = f.read() #读入文件内容，返回一个字符串
    length = len(file) #获得返回的字符串的长度
    filenames.append(filename)
    lenlist.append(length)
    f.close()

file_len = dict(zip(filenames, lenlist))


# In[23]:


#练习一 2.将上述字典以json字符串的形式存入文本文件中
import json
import codecs

fp = codecs.open('books/file_json.json', 'w', 'utf-8') 
json.dump(file_len,fp,ensure_ascii=False)
fp.close()


# In[24]:


#练习一 3. 将上述字典以pickle二进制形式存入文件中

import pickle

with open('books/file_pickle.pkl', "wb") as fp: 
    pickle.dump(file_len,fp)   


# In[ ]:





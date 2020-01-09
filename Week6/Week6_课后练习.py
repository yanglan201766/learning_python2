#!/usr/bin/env python
# coding: utf-8

# In[14]:


# 1.同样是读取练习一中的压缩包book.zip中解压缩后的文件，这次在命令行下传递参数，参数为需要读取的文件的文件名；
# 2.根据命令行下传递的 文件名读取文件；读取文件时使用异常处理的方法来解决不存在文件的异常情况（比如命令行输入了一个文件名，而引文件并不存在）
# 3.分别将读取的文件中的中文和英文分离开来，另存为两个文件；比如文件a.txt中既包含中文，也包含英文，将所有中文部分抽取出来，保存为a_CN.txt，将所有英文抽取出来 ，保存为a_EN.txt；以次类推。

import re
import os
import sys

filename = sys.argv[1] #命令行输入文件名，sys.argv[0]是运行程序的文件名

try:     
    f = open('E:/Learning_Python/workspace/learning_python2/book/books/'+filename)     
    name = filename[:-4]
    text = f.read()
    zh = re.sub(u"([\u0041-\u005a\u0061-\u007a]|[\.\'\"\‘\?\．])","",text)
    en = re.sub(u"([\u4e00-\u9fa5]|[\（\）\《\》\——\；\，\、\？\。\……\“\”\<\>\！\：\·\•])","",text)
    with open('E:/Learning_Python/workspace/learning_python2/'+name+'_ZH.txt', 'w') as fz:
        fz.write(zh)
    with open('E:/Learning_Python/workspace/learning_python2/'+name+'_EN.txt', 'w') as fe:
        fe.write(en)
except IOError:
    print ("File is not accessible.")


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[23]:


import os
import re
import json
import nltk
import sys
import jieba
import numpy as np
import pandas as pd
import jieba.posseg as pseg
from collections import Counter
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize


# In[24]:


#--------------------------英文-----------------------

#读取文件内容，返回文件内容
def ReadContent_en(fname):
    
    with open(fname, 'r', encoding = 'utf-8')as file_object:
        content = file_object.read()
        
    return content

#从文件内容中抽取5000个句子
def Extract_en(content):
    
    text = sent_tokenize(content)[0:5000]
    return text

#标注词性判断句型
def Judge_en(text):
    
    sens = []
    stype = []

    for j in text:
        sens.append(j)
        t = nltk.word_tokenize(j)
        tags = nltk.pos_tag(t)
        if (tags[0][1] == "WRB" or tags[0][1] == "WP") and (tags[-1][0] == "?"):
            stype.append("特殊疑问句")
        elif (tags[0][0]=="Did"or tags[0][0]=="Do"or tags[0][0]=="Does"or tags[0][0]=="Had"or tags[0][0]=="Has"or tags[0][0]=="How"or tags[0][0]=="Is" or tags[0][0]=="Am" or tags[0][0]=="Are") and (tags[1][1]=="PRP" or tags[1][1]=="DT" or tags[1][1]=="NN"or tags[1][1]=="NNS" or tags[1][1]=="NNP" or tags[1][1]=="NNPS" or tags[1][1]=="PRP$" ) and (tags[-1][0]=="?") and (tags[2][0]!="?"):
            stype.append("一般疑问句")
        elif (tags[0][0] == "How" or tags[0][0] == "What" ) and (tags[-1][0] == "!"):
            stype.append("感叹句")
        elif (tags[0][1] == "NN" or tags[0][1] == "NNS" or tags[0][1] == "NNP" or tags[0][1] == "NNPS" or tags[0][1] == "PRP" or tags[0][1] == "PRP$") and (tags[1][1] == "VB" or tags[1][1] == "VBD" or tags[1][1] == "VBP" or tags[1][1] == "VBZ") and (tags[2][1] == "NN" or tags[2][1] == "NNS" or tags[2][1] == "NNP" or tags[2][1] == "NNPS" or tags[2][1] == "PRP" or tags[2][1] == "PRP$") and (tags[-1][0]=="."):
            stype.append("主谓宾")
        elif (tags[0][0] == "There") and (tags[1][0] == "is" or tags[1][0] == "are" or tags[1][0] == "was" or tags[1][0] == "were") and (tags[-1][0]=="."):
            stype.append("there be句型")
        else:
            stype.append("未知")
    
    return sens,stype #抽取的5000个句子，5000个句子的句型

#将上述两个list整合成字典，导出成csv文件
def WriteContent_en(sens,stype):
    
    dataframe = pd.DataFrame({'sentence':sens,'type':stype})#抽取的5000个句子,每个句子的类型
    dataframe.to_csv("E:/Learning_Python/workspace/learning_python2/sen_en.csv",index=False,encoding='gbk',sep=',')


# In[25]:


#--------------------------中文-----------------------

#读取文件内容，返回文件内容
def ReadContent_zh(fname):
    
    with open(fname, 'r', encoding = 'gb18030')as file_object:
        content = file_object.read()
        
    return content

#从文件内容中抽取5000个句子
def Extract_zh(content):
    
    text = []
    temp = ''
    num = 0
    for i in content:
        temp+=i
        if (num < 5000) :
            if (i == "。" or i == "？" or i == "！"):
                num = num + 1
                text.append(temp)
                temp = ''
       
    return text


#判断句型
def Judge_zh(text):
    
    sens = []
    stype = []
    
    for j in text:
        sens.append(j)        
        if ("把" in j):
            stype.append("把字句")
        elif ("被" in j):
            stype.append("被字句")
        elif ("是" in j):
            stype.append("是字句")
        elif ("！" in j):
            stype.append("感叹句")
        elif ("？" in j):
            stype.append("疑问句")
        else :
            stype.append("未知")
                
    return sens,stype #抽取的5000个句子，5000个句子的句型


#将上述两个list整合成字典，导出成csv文件
def WriteContent_zh(sens,stype):
    
    dataframe = pd.DataFrame({'sentence':sens,'type':stype})#抽取的5000个句子,每个句子的类型
    dataframe.to_csv("E:/Learning_Python/workspace/learning_python2/sen_zh.csv",index=False,encoding='gbk',sep=',')


# In[26]:


#-------------------------------------------------    
    
def sentence_en(fname):
    """
    上述信息进行整合并输出
    """
    text_en=ReadContent_en(fname)
    sen_en=Extract_en(text_en)
    j_en=Judge_en(sen_en)
    WriteContent_en(j_en[0],j_en[1])
    
    
def sentence_zh(fname):
    """
    上述信息进行整合并输出
    """
    text_zh=ReadContent_zh(fname)
    sen_zh=Extract_zh(text_zh)
    j_zh=Judge_zh(sen_zh)
    WriteContent_zh(j_zh[0],j_zh[1])        


# In[27]:


sentence_en("E:/Learning_Python/workspace/learning_python2/en.txt")
sentence_zh("E:/Learning_Python/workspace/learning_python2/zh.txt")


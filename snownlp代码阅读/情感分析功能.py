#!/usr/bin/env python
# coding: utf-8

# In[ ]:


(/导入模块)

from __future__ import unicode_literals

import os
import codecs  //codecs专门用作编码转换

from .. import normal
from .. import seg
from ..classification.bayes import Bayes

data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sentiment.marshal')


# 分词—>训练—>分类

# In[ ]:


(/创建Sentiment类)
class Sentiment(object):

    def __init__(self):
        self.classifier = Bayes() 
        (/使用Bayes的模型)

    def save(self, fname, iszip=True):
        self.classifier.save(fname, iszip) 
        (/保存最终的模型)

    def load(self, fname=data_path, iszip=True):
        self.classifier.load(fname, iszip) 
        (/加载贝叶斯模型)

    (/分词以及去停用词的操作)
    def handle(self, doc):
        words = seg.seg(doc) //分词
        words = normal.filter_stop(words) //去停用词
        return words //返回分词后的结果，是一个list列表

    def train(self, neg_docs, pos_docs):
        data = []
        for sent in neg_docs:  //读入负样本
            data.append([self.handle(sent), 'neg'])
        for sent in pos_docs:  //读入正样本
            data.append([self.handle(sent), 'pos'])
        (/调用的是Bayes模型的训练方法)
        self.classifier.train(data)

    def classify(self, sent):
        (/调用Sentiment类中的handle方法和Bayes类中的classify方法)
        ret, prob = self.classifier.classify(self.handle(sent)) //调用贝叶斯中的classify方法
        if ret == 'pos':
            return prob
        return 1-prob


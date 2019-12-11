```python
#导入模块


from __future__ import unicode_literals 
#python 2中使用，__future__把下一个新版本的特性导入到当前版本，于是我们就可以在当前版本中测试一些新版本的特性

import sys
#sys模块包含了与Python解释器和它的环境有关的函数
import gzip
#gzip模块主要支持打开对应格式的压缩文件，并可以完成对压缩文件的读出和写入操作。
import marshal
#marshal模块负责在Python数值与二进制字节对象之间进行转换
from math import log, exp
#exp()函数返回参数的指数


from ..utils.frequency import AddOneProb
```

朴素贝叶斯（Naive Bayes）分类
其核心是计算条件概率P(y|x），其中y为类别，x为特征向量。其意义是在x样本出现时，它被划分为y类的可能性（概率）。
然后通过公式P(y|x) = P(y)* P(x|y)/P(x)，我们转化为计算在不同分类y下的x出现的概率，进而把样本划分到概率最大的一类。

P(c1∣w1,⋯,wn)==1/（1+exp[log(P(w1,⋯,wn∣c2)⋅P(c2))−log(P(w1,⋯,wn∣c1)⋅P(c1))])

朴素贝叶斯（Naive Bayes）分类在文本分类应用中的思路：
(1)建立词库，即无重复的单词表。
(2)分别计算词库中类别标签出现的概率P(y)。
(3)分别计算各个类别标签下不同单词出现的概率P(xi|y)。
(4)在不同类别下，将待分类样本各个特征出现概率P(xi|y)相乘，然后在乘以对应的P(y)。
(5)比较不同类别下（4）中结果，将待分类样本分到取值最大的类别。


```python
#创建Bayes类
class Bayes(object):

    #初始化函数
    def __init__(self):
    #self代表类的实例，而非类。类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
        self.d = {}
        #用字典进行分类记录
        self.total = 0
        #值为单词总数
```


```python
    #保存已分类处理文本的总词数、各个类别及类别对应的总词数
    def save(self, fname, iszip=True):
        d = {}
        d['total'] = self.total
        d['d'] = {}
        for k, v in self.d.items():
        #dict.items()以列表返回可遍历的(键, 值) 元组数组
            d['d'][k] = v.__dict__
        #__dict__用于查看对象内部存储的所有属性名和属性值组成的字典
        if sys.version_info[0] == 3:
        #sys.version_info获取Python解释程序的版本信息
            fname = fname + '.3'
        if not iszip:
            marshal.dump(d, open(fname, 'wb'))
            #marshal.dump(value, file[, version])，将值写入到一个打开的输出流里。参数value表示待序列化的值。file表示打开的输出流。如:以”wb”模式打开的文件
        else:
            f = gzip.open(fname, 'wb')
            f.write(marshal.dumps(d))
            f.close
```


```python
    #加载文本的总词数、各个类别及类别对应的总词数
    def load(self, fname, iszip=True):
        if sys.version_info[0] == 3:
            fname = fname + '.3'
        if not iszip:
            d = marshal.load(open(fname, 'rb'))
        else:
            try:
                f = gzip.open(fname, 'rb')
                d = marshal.loads(f.read())
            except IOError:
                f = open(fname, 'rb')
                d = marshal.loads(f.read())
            f.close()
        self.total = d['total']
        self.d = {}
        for k, v in d['d'].items():
            self.d[k] = AddOneProb()
            self.d[k].__dict__ = v
```


```python
#创建BaseProb和AddOneProb类
class BaseProb(object):
 
     def __init__(self):
         self.d = {}#用来存储分词和分词的个数，键是分词，值是分词的个数
         self.total = 0.0#计数总共的词个数
         self.none = 0
 
     def exists(self, key):#判断字典self.d中是否存在这个词key
         return key in self.d
 
     def getsum(self):#返回语self.d中存储的词的总数
         return self.total
 
     def get(self, key):#判断字典中是否存在这个词key,并且返回这分词的词个数
         if not self.exists(key):
             return False, self.none
         return True, self.d[key]
 
     def freq(self, key):#计算词key的频率
         return float(self.get(key)[1])/self.total
 
     def samples(self):#返回字典的键，其实就是返回所有的分词，以列表形式
         return self.d.keys()
 
 class NormalProb(BaseProb):
 
     def add(self, key, value):
         if not self.exists(key):
             self.d[key] = 0
         self.d[key] += value
         self.total += value
 
 '''对词计数'''
 class AddOneProb(BaseProb):#继承BaseProb类，所以BaseProb类中的属性和函数都能用。
 
     def __init__(self):
         self.d = {}
         self.total = 0.0
         self.none = 1
 
     def add(self, key, value):
         self.total += value#计算总词数
         if not self.exists(key):#如果这个词key不在self.d中的话，那么在字典中加上这个词，即键为此，并且给这个词计数1，同时总的词数量total加1.
             self.d[key] = 1
             self.total += 1#感觉不应该再加1了，上面都已经计算过总数了？？？？说是后面预测要用到，可能是要平滑
         self.d[key] += value#如果字典已经有这个词了的话，那么给这个词数量加1
```


```python
    #训练函数
    def train(self, data):
    #训练的数据data格式是[[['分词1','分词2','分词x'],类别],[[第二行分词], 类别],...,[[第n行分词],类别]]    
    #data=[d0,d1,d2,......,dn]
    #d0=[[分词结果列表],类别]
        for d in data:
            c = d[1]#d[0]是分词的结果，是一个列表
            #判断数据字典中是否有当前的标签
            if c not in self.d:
                self.d[c] = AddOneProb()
                #如果没有该标签，加入标签，值是一个AddOneProb对象。其实就是为每个分词建一个AddOnePro对象来计数
            for word in d[0]:
                self.d[c].add(word, 1)
                #调用AddOneProb中的add方法，添加单词
        self.total = sum(map(lambda x: self.d[x].getsum(), self.d.keys()))
        #lambda就是用来定义一个匿名函数的
        #self.d[x].getsum()是调用AddOneProb对象的getsum()函数计算词数。这行代码是计算所有的d中的sum之和
```


```python
    #文本分类函数
    def classify(self, x):
    #x是被分过词的列表
        tmp = {}
        #key:类别；value:该类别出现的次频的log值
        for k in self.d:
            tmp[k] = log(self.d[k].getsum()) - log(self.total)
            #获取每个分类标签下的总词数和所有标签总词数，求对数差相当于log（某标签下的总词数/所有标签总词数）
            for word in x:
                tmp[k] += log(self.d[k].freq(word))
            #获取每个单词出现的频率，log[（某标签下的总词数/所有标签总词数）*单词出现频率]，word不在字典里的话词频就为0
        ret, prob = 0, 0
        for k in self.d:
            now = 0  #预测值赋初值为0
            try:
                for otherk in self.d:
                    now += exp(tmp[otherk]-tmp[k])
                    #当类相同时now=1，类不同时now累加exp（tmp[otherk]-tmp[k]），最终计算now为变形后的朴素贝叶斯预测值的分母
                    #exp()方法返回x的指数,e^x
                now = 1/now  #求倒数为得到的这个类的预测值
            except OverflowError:
                now = 0
            if now > prob:  #比较两个类别的概率谁大，大的就是这个文本的类别。注意：初始prob等于0，经过遍历后会更新prob并且prob等于相应类别的朴素贝叶斯概率
                ret, prob = k, now
        return (ret, prob)
```

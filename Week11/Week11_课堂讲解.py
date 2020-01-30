#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests
import random
import time
from pyquery import PyQuery as pq

class ProxyPool():
    def __init__(self):
        # 初始化读取proxy站点配置文件

        # 初始化读取proxy池存储位置（文件、数据库、NoSQL...)

        # 定时扫描proxy可用性、删除失效代理
        pass

    def check_a_proxy(self):
        pass

class KKBaseDownloader():
    def __init__(self):
        # 初始化代理池对象
        self.proxyp = ProxyPool()
        # 初始化headers配置列表文件路径
        self.headers_cfg_pth=''
        # 初始化最小、最大暂停间隔
        self.interval_min_max = (5,30)
        pass
    
    def gen_an_ua(self):
        self.ua_list = ["Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0"]

        return random.choice(self.ua_list)

    def get_a_proxy(self):
        proxys = [

        ]
        idx = random.randint(1,len(proxys))
        return proxys[idx]

class KKNavDl(KKBaseDownloader):
    def __init__(self,init_url):
        super(KKNavDl,self).__init__()  #调用父类的实体化
        self.url_tgt = init_url  #定义为自己的url

    def fetch_html(self):
        ua = self.gen_an_ua()   #继承父类的方法
        headers = {'User-Agent':ua}
        # _proxy = self.get_a_proxy()
        # r = requests.get(self.url_tgt,proxies=_proxy)
        r = requests.get(self.url_tgt,headers=headers) #获取网页
        if r.status_code==200:
            if r.encoding == 'ISO-8859-1':
                encodings = requests.utils.get_encodings_from_content(r.text)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = r.apparent_encoding  #解决编码问题
            encode_content = r.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            return encode_content
        else:
            return ''

#基类
class KKBaseExtractor():  
    def __init__(self,html='<html></html>'):
        self.doc = pq(html)  #pquery的一个对象实例 

class KKNavExt(KKBaseExtractor):
    def __init__(self,html):
        super(KKNavExt,self).__init__(html)  

    def parse(self):  #抽取导航栏
        lis = self.doc('.navtab>ul>li')
        nav_links = []
        for i in range(3,len(lis)):
            pq_li = pq(lis[i])
            nav_links.append((pq_li.text(),pq_li.find('a').attr('href')))
        return nav_links


navDl = KKNavDl(init_url='http://www.kekenet.com/read/news/')
html = navDl.fetch_html()
navExt = KKNavExt(html)
nav_links = navExt.parse()
for lnk in nav_links:
    print(lnk)
    


# In[11]:


import requests
import random
import time
from pyquery import PyQuery as pq

class ProxyPool():
    def __init__(self):
        # 初始化读取proxy站点配置文件

        # 初始化读取proxy池存储位置（文件、数据库、NoSQL...)

        # 定时扫描proxy可用性、删除失效代理
        pass

    def check_a_proxy(self):
        pass

class KKBaseDownloader():
    def __init__(self):
        # 初始化代理池对象
        self.proxyp = ProxyPool()
        # 初始化headers配置列表文件路径
        self.headers_cfg_pth=''
        # 初始化最小、最大暂停间隔
        self.interval_min_max = (5,30)
        pass
    
    def gen_an_ua(self):
        self.ua_list = ["Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0"]

        return random.choice(self.ua_list)

    def get_a_proxy(self):
        proxys = [

        ]
        idx = random.randint(1,len(proxys))
        return proxys[idx]

class KKNavDl(KKBaseDownloader):
    def __init__(self,init_url):
        super(KKNavDl,self).__init__()  #调用父类的实体化
        self.url_tgt = init_url  #定义为自己的url

    def fetch_html(self):
        ua = self.gen_an_ua()   #继承父类的方法
        headers = {'User-Agent':ua}
        # _proxy = self.get_a_proxy()
        # r = requests.get(self.url_tgt,proxies=_proxy)
        r = requests.get(self.url_tgt,headers=headers) #获取网页
        if r.status_code==200:
            if r.encoding == 'ISO-8859-1':
                encodings = requests.utils.get_encodings_from_content(r.text)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = r.apparent_encoding  #解决编码问题
            encode_content = r.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            return encode_content
        else:
            return ''

#基类
class KKBaseExtractor():  
    def __init__(self,html='<html></html>'):
        self.doc = pq(html)  #pquery的一个对象实例 

class KKNavExt(KKBaseExtractor):
    def __init__(self,html):
        super(KKNavExt,self).__init__(html)  

    def parse(self):  #抽取导航栏
        lis = self.doc('.box>ul>li>h2')
        nav_links = []
        for i in range(3,len(lis)):
            pq_li = pq(lis[i])
            nav_links.append((pq_li.text(),pq_li.find('a').attr('href')))
        return nav_links


navDl = KKNavDl(init_url='http://www.kekenet.com/read/news/')
html = navDl.fetch_html()
navExt = KKNavExt(html)
nav_links = navExt.parse()
for lnk in nav_links:
    print(lnk)
    


# In[19]:


import pymysql
conn = pymysql.connect('localhost','root','','kekenet')
cur = conn.cursor()
sql = 'set names utf8'
cur.execute(sql)

sql = 'select * from article'
cur.execute(sql)

dat = cur.fetchall()
print(dat)


# In[26]:


conn.commit()
cur.close()
conn.close()


# In[27]:


conn = pymysql.connect('localhost','root','','kekenet')
cur = conn.cursor()
sql = 'set names utf8'


# In[28]:


sql = 'insert into article (id, title, editor, source, datetime, txt_en, txt_cn) values (3, "近一半的上班族因为压力太大而濒临崩溃", "Kelly", "chinadaily", "2019-10-12 07:00:00", "Nearly half of all employees are close to \"breaking point\" at work due to increased stress levels. A survey of 2,000 professionals found the average working adult feels stressed for almost a third of their working day.", "近一半的上班族因为压力增大而濒临崩溃。一项针对2000名职场人士的研究发现：工作日期间，每位上班族平均有三分之一的时间感到心力交瘁。")';
cur.execute(sql)
sql = 'select * from article'
cur.execute(sql)
data = cur.fetchall()
print('插入了一条数据:')
print(data)
print("\n")


# In[ ]:





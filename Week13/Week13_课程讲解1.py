#!/usr/bin/env python
# coding: utf-8

# In[1]:


import threading
def run(n):
    print('current task',n)
    
t1 = threading.Thread(target=run,args=("thread1",))
t2 = threading.Thread(target=run,args=("thread2",))

t1.start()
t2.start()


# In[2]:


from multiprocessing import Process

def show(name):
    print("Process name is " + name)
    
proc = Process(target=show, args=('subprocess'))
proc.start()


# In[3]:


from multiprocessing import Process, Queue

q = Queue()
for i in range(10):
    q.put(i)  
q


# In[4]:


q.get()


# In[5]:


q.get()


# In[6]:


def run(n):
    print('I get {} from queue'.format(str(n)))
    
p = []
for j in range(8):
    n = q.get()
    pj = Process(target=run,args=(n,))
    pj.start()
    p.append(pj)
for pj in p:
    pj.join()


# In[10]:


from nltk.util import ngrams
a = "add domain with authentication for conference focus user".split(' ')


# In[11]:


a


# In[12]:


unigram = ngrams(a,1)
unigram


# In[13]:


print([i for i in unigram])


# In[15]:


bigram = ngrams(a,2)
print([i for i in bigram])


# In[16]:


trigram = ngrams(a,3)
print([i for i in trigram])


# In[ ]:





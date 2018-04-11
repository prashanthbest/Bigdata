
# coding: utf-8

# In[2]:


def SUM(x,y):
    print(x+y)


# In[9]:


def TABLE(x):
    for i in range(10):
        print(x*(i+1))


# In[15]:


def SEARCHING(x,y):
    z=0
    for i in y:
        if (x==i):
            print(z)
        z=z+1


# In[10]:


TABLE (21)


# In[11]:


SUM(10,20)


# In[16]:


SEARCHING(30,[10,20,30,40,50])


# In[41]:


def serach(username):
    dict1={"aaaa":123,"bbbb":345,"cccc":567}
    dict2=dict1.keys()
    for i in dict2:
            if(i==username):
                print(dict1[i])


# In[45]:


serach("bbbb")


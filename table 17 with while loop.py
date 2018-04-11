
# coding: utf-8

# In[6]:


for a in range(10):
    print (a)


# In[4]:


print (a)


# In[8]:


b=10
c=0
while(c<=b):
    print(c)
    c=c+1


# In[10]:


z=17
for i in range(10):
    print("%d*%d=%d" %(z,(i+1),z*(i+1)))


# In[18]:


m=[10,25,35,45,67,85]
n=45
for i in range(len(m)):
    if(m[i]==n):
        print("index is", i)
        break


# In[19]:


s=[10,32,45,67,83,49,19]
x=0
f=67
g=83

for i in range(len(s)):
    if(s[i]==f):
        print("index is",i)
        x=x+1
        continue
    if(s[i]==g):
        print("index is",i)
        x=x+1
        continue
    if(x==2):
        break


# In[22]:


v=17
while i in range(10):
    print("%d*%d=%d" %(v,(i+1),v*(i+1)))


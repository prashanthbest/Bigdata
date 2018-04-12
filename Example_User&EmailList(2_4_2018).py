
# coding: utf-8

# In[2]:


un=["donthi.mahesh","rajurock4u","bujji123_m","prashanth_ch123","sreenath.123"]
eid=["donthi.mahesh@gmail.com","rajurock4u@gmail.com","bujji123_m@yahoo.com","prashanth_ch123@rediff.com","sreenath.123@gmail.com"]
    


# In[10]:


import re
class EmailExist(Exception):
    def __str__(self):
         self.value="Email Found"
         return(self.value)
class UserExist(Exception):
    def __str__(self):
        self.value="User Exist"
        return(self.value)
try:
    un1=input("Enter User Name:")
    eid1=input("enter email ID:")
    regex="(.*)@(.*)\.(.*)"
    match=re.match(regex,eid1)
    b=match.group(1)
    for i in eid:
        match=re.match(regex,i)
        x=match.group(1)
        for j in un:
            if x==b and un1==j:
                raise EmailExist
            else:
                m=0
    if m==0:
        print("user not found")
except EmailExist:
    raise
except UserExist:
    raise


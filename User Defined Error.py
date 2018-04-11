
# coding: utf-8

# In[1]:


class ExceedLength(Exception):
    def __init__(self):
        self.value="you have exceeded the specified limit"
    def __str__(self):
        return(self.value)


# In[5]:


try:
    x=input("enter name:")
    if len(x)>=11:
        raise ExceedLength
except ExceedLength as EL:
    raise EL


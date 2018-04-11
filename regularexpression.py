
# coding: utf-8

# In[6]:


import re
text="Sachin tendulkar 36"
regex="([A-z]+) ([a-z]+) ([0-9]+)"

match=re.match(regex,text)
print(match.group(0))
print(match.group(1))
print(match.group(2))
print(match.group(3))


# In[27]:


import re
text="sachin2314@gmail.com"
regex="(.*)@(.*)\.(.*)"

match=re.match(regex,text)
print(match.group(0))
print(match.group(1))
print(match.group(2))
print(match.group(3))


# In[28]:


import re
text="IMG 231017"
regex="[A-Z]+ [0-9][0-9][0-9][0-9][0-9][0-9]"

match=re.match(regex,text)

print(match.group(0))


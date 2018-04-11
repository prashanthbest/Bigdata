
# coding: utf-8

# # Print a table of 2 only till 10. If 11 then "TillTen" Exception
# class TillTen(Exception):
#     def __str__(self):
#         self.value="Till Ten excepton"
#         return(self.value)

# In[44]:


try:
    m=2
    for i in range(12):
        if i<9:
            print("%d X %d = %d" %(m,(i+1),m*(i+1)))
        else:
            raise TillTen            
except TillTen:
    raise


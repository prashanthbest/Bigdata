
# coding: utf-8

# In[12]:


# Multi Threading Example






# In[18]:



import threading

def add(x,y):

    print("Sum is:",x+y)

def diff(x,y):

    print("Difference is:",x-y)

def product(x,y):

    print("Product is:",x*y)

def main_task(x,y):

    t1=threading.Thread(target=diff,args=(x,y))

    t2=threading.Thread(target=add,args=(x,y))

    t3=threading.Thread(target=product,args=(x,y))

    t1.start()

    t2.start()

    t3.start()

    t1.join()

    t2.join()

    t3.join()

    print("done")


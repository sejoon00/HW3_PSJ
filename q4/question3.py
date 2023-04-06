#!/usr/bin/env python
# coding: utf-8

# In[6]:


def fact(n):
    if n<1 :
        return 1
    else :
        return n * fact(n-1)

if __name__ == "__main__":
    ans =0 
    for i in range(0,8):
        ans = fact(i*2)
        print("fact(",i*2,") : ",ans)


# In[ ]:





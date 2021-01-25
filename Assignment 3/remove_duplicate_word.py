#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Python program to remove all duplicates words from a given sentence
sample_string="my name is rahul chauhan rahul"
sample_string=sample_string.lower()
slist = sample_string.split()
print(" ".join(sorted(set(slist), key=slist.index)))


# In[ ]:





# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[16]:


# Python program to find all occurrences of a character in the given string
def find_occurrences(a, b):
    print('Below are the location where {} is available'.format(b))
    return [i for i, letter in enumerate(a) if letter == b]
a = input('Enter the string value: ')
b = input('Enter the character name for which occurence need to find')
find_occurrences(a, b)


# In[ ]:





# In[ ]:





# In[ ]:





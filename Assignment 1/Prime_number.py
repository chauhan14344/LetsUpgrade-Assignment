#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python Program to print Prime Numbers from 1 to 10
num = 1
while(num <= 10):
    count = 0
    i = 2
    
    while(i <= num//2):
        if(num % i == 0):
            count = count + 1
            break
        i = i + 1

    if (count == 0 and num != 1):
        print(" %d" %num, end = '  ')
    num = num  + 1


# In[ ]:





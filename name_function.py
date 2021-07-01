#!/usr/bin/env python
# coding: utf-8

# In[1]:


def get_formatted_name(first, last, middle=''):
    """生成整洁的姓名"""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()


# In[ ]:





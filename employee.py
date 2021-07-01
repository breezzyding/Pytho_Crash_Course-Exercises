#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Employee():
    """收集雇员信息""" 
    
    def __init__(self, f_name, l_name, pay):   
        """信息包括姓名和年薪"""
        self.f_name = f_name
        self.l_name = l_name
        self.pay = pay
        
    def give_raise(self, pay_rise=5000):
        """增加年薪"""
        self.pay += pay_rise
        


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def get_city_country(city, country, population=''):
    """获取城市名字和所属国家"""
    if population:
        city_country = city + ", "  + country + " - Population " + str(population)
    else:
        city_country = city + ", "  + country
    return city_country.title()


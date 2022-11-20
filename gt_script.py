# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 19:58:22 2022

@author: rapha
"""

# pytrend precisa de algumas lib para rodar:
'''
pip install pytrends # Unofficial API for Google Trends.
pip install requests # Requests is a simple, yet elegant, HTTP library.
pip install lxml # As an XML library, lxml is often used under the hood of in-house server applications.
pip install pandas
'''


from pytrends.request import TrendReq
import pandas as pd


pytrend = TrendReq(hl='pt-BR')

kw_list = []

cat = 0

timeframe = 'today 5-y'

geo = ''

gprop=''

pytrends.build_payload(kw_list,
                       cat,
                       timeframe,
                       geo, 
                       gprop)


df = pd.DataFrame(keywords)

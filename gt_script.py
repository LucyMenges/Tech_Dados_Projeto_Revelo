# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 19:58:22 2022

@author: rapha
"""

# pip install pytrends

import pytrends
import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq()

keywords = pytrend.suggestions(keyword='SQL')

df = pd.DataFrame(keywords)

#provide your search terms
kw_list=['SQL', 'Python', 'PowerBI', 'Data', 'SQLite']

#search interest per region
#run model for keywords (can also be competitors)
pytrend.build_payload(kw_list, timeframe='today 1-m')

# Interest by Region
regiondf = pytrend.interest_by_region()
#looking at rows where all values are not equal to 0
regiondf = regiondf[(regiondf != 0).all(1)]

#drop all rows that have null values in all columns
regiondf.dropna(how='all',axis=0, inplace=True)

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 19:58:22 2022

@author: rapha

base: https://www.youtube.com/@Pythonenthusiast
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

## chamar a lib e setar os argumentos:
# solicitar e definir a linguagem, 'en-US', 'pt-BR'.
pytrends = TrendReq(hl='pt-BR', timeout=(30,60), retries=2)

# montar lista de palavras que vamos analisar. Nomalmente o google trends limitaria em até 5 correlações entre as palavra, mas vamos expandir isso...
all_keywords = ['SQL', 'Python',
                'DBeaver', 'Power BI',
                'Pandas', 'Data Analist']

dict_1 = {'word_ak':all_keywords, 'df_it':[], 'df_r':[], 'mean_df_it':[]}

# qual o periodo de tempo que iremos buscar no passado.
timeframe = ['all', 'today 5-y', 'today 12-m',
             'today 3-m', 'today 1-m', 'now 7-d',
             'now 1-d']

# se vamos ou nao solicitar uma categoria especial, cat = '0' All Categories; cat = '8'' Games, etc.
cat = '0'

# se vamos optar em regiao do globo em especifico, .
geo = ['', 'BR', 'US']

# se vamos buscar em algum lugar especifico dentro do google, como websearch (defaut), youtube, news e shopping..
gprop = ''

def check_trends(kw):
    # funcao para correr o interest_over_time
    pytrends.build_payload([kw], cat, timeframe[2], geo[1], gprop)
    data = pytrends.interest_over_time()
    # data2 = pytrends.interest_by_region(resolution='BRAZIL', inc_low_vol=True, inc_geo_code=False)
    return data #(data, data2)

# para correr cada palavra inserida na lista em separado 
for kw in all_keywords:
    data = check_trends(kw)
    # data, data2 = check_trends(kw)
    dict_1['df_it'].append(data)
    # dict_1['df_r'].append(data2)

for kdf in dict_1['df_it']:
    dict_1['mean_df_it'].append(kdf.iloc[:0].mean())




















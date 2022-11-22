# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 19:58:22 2022

@author: rapha

references:
    https://trends.google.com/
    https://pypi.org/project/pytrends/#api-methods
    https://www.youtube.com/@Pythonenthusiast
    https://lazarinastoy.com/the-ultimate-guide-to-pytrends-google-trends-api-with-python/
"""

# pytrend precisa das seguintes libs:
'''
pip install pytrends # Unofficial API for Google Trends.
pip install requests # Requests is a simple, yet elegant, HTTP library.
pip install lxml # As an XML library, lxml is often used under the hood of in-house server applications.
pip install pandas
'''
from pytrends.request import TrendReq

# para carregar os argumentos do payload, o payload vai ser usado para todas as funcoes da lib:
# vamos definir a linguagem, 'en-US', 'pt-BR' e regra de conexao.
pytrends = TrendReq(hl='pt-BR', timeout=(30, 60), retries=2)

# vamos montar lista de palavras que vamos analisar. Nomalmente o google trends limitaria de 1 até 5 palavra, mas vamos expandir isso...
keywords_list = ['SQL', 'Python',
                 'Power BI', 'Pandas']

data_dict = {'df_keyword': keywords_list, 'df_it': [],
             'df_ir': [], 'df_rt': [], 'df_rq': []}

# vamos definir qual o periodo de tempo que iremos buscar no passado.
timeframe = ['all', 'today 5-y', 'today 12-m',
             'today 3-m', 'today 1-m', 'now 7-d',
             'now 1-d']

# se vamos ou nao solicitar uma categoria especial, cat = '0' All Categories; cat = '8'' Games, etc.
cat = '0'

# se vamos optar em regiao do globo em especifico, .
geo = ['', 'BR', 'US']

# se vamos buscar em algum lugar especifico dentro do google, como websearch (defaut), youtube, news e shopping..
gprop = ''

# para setar os agumento de interest_by_region
# o nível que iremos buscar a informacao
resolution = ['CITY', 'COUNTRY', 'REGION', 'DMA']

# se vamos incluir, ou nao, volume pequenos por paises/regioes
inc_low_vol = [True, False]

# se vamos incluir, ou nao, o codigo ISO dos paises e o nome da data
inc_geo_code = [True, False]


def check_trends(kw):
    # o payload:
    pytrends.build_payload([kw], cat, timeframe[2], geo[1], gprop)
    # definindo funcoes da lib pytrends:
    data_it = pytrends.interest_over_time()
    data_ir = pytrends.interest_by_region(resolution[0],
                                          inc_low_vol[1],
                                          inc_geo_code[0])
    data_rt = pytrends.related_topics()
    data_rq = pytrends.related_queries()
    return data_it, data_ir, data_rt, data_rq


# para ciclar cada kw inserida na keywords_list, extrair resultado como df e inserir no data_dict
for kw in keywords_list:
    data_it, data_ir, data_rt, data_rq = check_trends(kw)
    data_dict['df_it'].append(data_it)
    data_dict['df_ir'].append(data_ir)
    data_dict['df_rt'].append(data_rt)
    data_dict['df_rq'].append(data_rq)

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 19:58:22 2022

@author: rapha

"""
## @package check_trends
# Metodo para utilizar a lib PyTrends para analisar 
'''
references:
    https://trends.google.com/
    https://pypi.org/project/pytrends/#api-methods
    https://www.youtube.com/@Pythonenthusiast
    https://lazarinastoy.com/the-ultimate-guide-to-pytrends-google-trends-api-with-python/
'''

# Bibliotecas que pytrend precisa das seguintes libs: requests, lxml, pytrends.

# @param kw: Palavra chave coletada para ser analizada no Google Trends

from pytrends.request import TrendReq
pytrends = TrendReq(hl='pt-BR', timeout=(30, 60), retries=2)

def check_trends(kw, timeframe, geo, resolution, inc_low_vol, inc_geo_code):
    # carregando payload:
    pytrends.build_payload([kw], cat, timeframe, geo, gprop)
    # carregando as funcoes da lib:
    data_it = pytrends.interest_over_time()
    data_ir = pytrends.interest_by_region(resolution, inc_low_vol, inc_geo_code)
    data_rt = pytrends.related_topics()
    data_rq = pytrends.related_queries()
    return data_it, data_ir, data_rt, data_rq
    # @return 


# para carregar os argumentos do payload, o payload vai ser usado para todas as funcoes da lib:
# vamos definir a linguagem, 'en-US', 'pt-BR' e regra de conexao.


# vamos montar lista de palavras que vamos analisar. Nomalmente o google trends limitaria de 1 até 5 palavra, mas podemos expandir isso...
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



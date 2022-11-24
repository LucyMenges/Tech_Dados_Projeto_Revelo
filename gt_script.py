# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 19:58:22 2022

@author: rapha

"""

# Metodos para utilizar a lib PyTrends para analisar palavras-chave no Google Trends

"""
references:
    https://trends.google.com/
    https://pypi.org/project/pytrends/#api-methods
    https://www.youtube.com/@Pythonenthusiast
    https://lazarinastoy.com/the-ultimate-guide-to-pytrends-google-trends-api-with-python/
"""

# Pytrend precisa das seguintes libs para funcionar: requests, lxml, pytrends.

# Preparando a TrendReq():
# @param hl: str
# @param timeout: int, tuple, str 
# @param retries: int
from pytrends.request import TrendReq
pytrends = TrendReq(hl='pt-BR', timeout=(30, 60), retries=2)


# Preparando o build_payload():
# @param kw:
    # str, é a palavra chave coletada para ser analizada no Google Trends.
# @param cat:
    # str, define a categoria para refinar a pesquisa, defaut é sem categoria definida 
    # wiki para todas: https://github.com/pat310/google-trends-api/wiki/Google-Trends-Categories
# @param timeframe:
    # str, define periodo para busca.
    # 'all', 'today 5-y', 'today 12-m', 'today 3-m', 'today 1-m', 'now 7-d', 'now 1-d'
# @param geo:
    # str, identificacao paises padrao de 2 letras, Brasil = 'BR', pode ser refinado com a regiao Parana = 'BR-PR', etc. 
# @param gprop: 
    # str, propriedade Google onde a busca deve ser realizada: 'images', 'news', 'youtube' or 'froogle' (para Google Shopping)


# interest_over_time()
def check_interest_over_time(kw, cat, timeframe, geo, gprop):
    pytrends.build_payload(kw, cat, timeframe, geo, gprop)
    data_it = pytrends.interest_over_time()
    return data_it

# interest_by_region()
resolution = ['CITY', 'COUNTRY', 'REGION', 'DMA']
inc_low_vol = [True, False]
inc_geo_code = [True, False]

def check_interest_by_region(kw, cat, timeframe, geo, gprop, resolution, inc_low_vol, inc_geo_code):    
    pytrends.build_payload(kw, cat, timeframe, geo, gprop)
    data_ir = pytrends.interest_by_region(resolution, inc_low_vol, inc_geo_code)
    return data_ir

# related_topics()
def check_related_topics(kw, cat, timeframe, geo, gprop):
    pytrends.build_payload(kw, cat, timeframe, geo, gprop)
    data_rt = pytrends.related_topics()
    return data_rt

# related_queries()
def check_trends(kw, cat, timeframe, geo, gprop):
    pytrends.build_payload(kw, cat, timeframe, geo, gprop)
    data_rq = pytrends.related_queries() 
    return data_rq







# -*- coding: utf-8 -*-

# @packge gt_script

# Modulo para utilizar a lib PyTrends e agrupar metodos para analisar palavras-chave no Google Trends.

#references:
# https://trends.google.com/
# https://pypi.org/project/pytrends/#api-methods
# https://www.youtube.com/@Pythonenthusiast
# https://lazarinastoy.com/the-ultimate-guide-to-pytrends-google-trends-api-with-python/

# Pytrend precisa das seguintes libs para funcionar: requests, lxml, pytrends.

# Preparando a TrendReq():
from pytrends.request import TrendReq
pytrends = TrendReq(hl='pt-BR', timeout=(30, 60), retries=2)

## check_trends
#
# Esse metodo obtem o interesse de uma...
#
# @param kw: str, é a palavra chave coletada para ser analizada no Google Trends.
# @param cat: str, define a categoria para refinar a pesquisa, defaut é sem categoria definida, wiki para todas: https://github.com/pat310/google-trends-api/wiki/Google-Trends-Categories
# @param timeframe: str, define periodo para busca:'all', 'today 5-y', 'today 12-m', 'today 3-m', 'today 1-m', 'now 7-d', 'now 1-d'
# @param geo: str, identificacao paises padrao de 2 letras, Brasil = 'BR', pode ser refinado com a regiao Parana = 'BR-PR', etc. 
# @param gprop: str, propriedade Google onde a busca deve ser realizada: 'images', 'news', 'youtube' or 'froogle' (para Google Shopping)
# @param resolution = ['CITY', 'COUNTRY', 'REGION', 'DMA']
# @param inc_low_vol = [True, False]
# @param inc_geo_code = [True, False]
#
# @return data_it:
# @return data_ir:
# @return data_rt:
# @return data_rq:
#
def check_trends(kw, cat, timeframe, geo, gprop, resolution, inc_low_vol, inc_geo_code):
    pytrends.build_payload([kw], cat, timeframe, geo, gprop)
    data_it = pytrends.interest_over_time()
    data_ir = pytrends.interest_by_region(resolution, inc_low_vol, inc_geo_code)
    data_rt = pytrends.related_topics()
    data_rq = pytrends.related_queries()
    return data_it, data_ir, data_rt, data_rq




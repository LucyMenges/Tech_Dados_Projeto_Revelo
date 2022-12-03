# -*- coding: utf-8 -*-

# @packge gt_script

# Modulo para utilizar a lib PyTrends e agrupar metodos para analisar palavras-chave no Google Trends.

# Referecias:
# https://trends.google.com/
# https://pypi.org/project/pytrends/#api-methods : https://github.com/GeneralMills/pytrends
# https://www.youtube.com/@Pythonenthusiast
# https://lazarinastoy.com/the-ultimate-guide-to-pytrends-google-trends-api-with-python/

# Pytrend depende da instalação das seguintes bibliotecas: requests, lxml, pytrends, pandas.
#
from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', timeout=(30, 60), retries=2)

# check_trends
#
# Esse metodo obtem aplica a pesquisa e leitura de uma lista de palavras-chaves nas funções, interest_over_time, interest_by_region, related_topics e related_queries da biblioteca PyTrends.
#
# @param kw: str, a palavra-chave para ser analizada no Google Trends.
# @param cat: str, define a categoria para refinar a pesquisa, defaut é sem categoria definida, wiki para todas: https://github.com/pat310/google-trends-api/wiki/Google-Trends-Categories
# @param timeframe: str, define periodo para busca, ex.:'all', 'today 5-y', 'today 12-m', 'today 3-m', 'today 1-m', 'now 7-d', 'now 1-d', 'now 4-h'.
# @param geo: str, identificacao de paises padrao de 2 letras, Brasil = 'BR', pode ser refinado com a regiao Parana = 'BR-PR', etc.
# @param gprop: str, propriedade Google onde a busca deve ser realizada: 'images', 'news', 'youtube' or 'froogle' (para Google Shopping)
# @param resolution = str, pesquisa em diferentes níves de resolução, cidade: 'CITY', pais : 'COUNTRY', regiao: 'REGION', e regiao metropolitana: 'DMA'.
# @param inc_low_vol = boolen, inclui ou não, pequenos volumes de busca em relação ao todo.
# @param inc_geo_code = boolen, inclue ou não, codigos ISO dos paises.
#
# @return data_it: dataframe.
# @return data_ir: dataframe.
# @return data_rt: dicionario, com duas dataframes.
# @return data_rq: dicionario, com duas dataframes.
#
def check_trends(kw, cat, timeframe, geo, gprop, resolution, inc_low_vol, inc_geo_code):
    pytrends.build_payload([kw], cat, timeframe, geo, gprop)
    data_it = pytrends.interest_over_time()
    data_ir = pytrends.interest_by_region(
        resolution, inc_low_vol, inc_geo_code)
    data_rt = pytrends.related_topics()
    data_rq = pytrends.related_queries()
    
    return data_it, data_ir, data_rt, data_rq

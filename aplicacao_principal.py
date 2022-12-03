# -*- coding: utf-8 -*-
from time import sleep
import gt_script as gt

keywords_list = ['SQL', 'Python',
                 'Power BI', 'Pandas']

data_dict = {'keywords': keywords_list, 'df_it': [],
             'df_ir': [], 'df_rt': []}

for kw in keywords_list:
    data_it, data_ir, data_rt, data_rq = gt.check_trends(
        kw, cat='0', timeframe='today 12-m', geo='BR', gprop='',
        resolution='COUNTRY', inc_low_vol=False, inc_geo_code=True)
    data_dict['df_it'].append(data_it)
    data_dict['df_ir'].append(data_ir)
    data_dict['df_rt'].append(data_rt)
    sleep(30)




"""
3. e 4.  habilidades

5. e 6. ferramentas

7. trends

SQL = data_dict['df_ir'][0]
Python = data_dict['df_ir'][1]
Power BI = data_dict['df_ir'][2]
Pandas = data_dict['df_ir'][3]


"""
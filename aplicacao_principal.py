# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 08:55:44 2022

@author: rapha
"""

import gt_script as gt

keywords_list = ['SQL', 'Python',
                 'Power BI', 'Pandas']

data_dict = {'df_keyword': keywords_list, 'df_it': [],
             'df_ir': [], 'df_rt': [], 'df_rq': []}

for kw in keywords_list:
    data_it = gt.check_interest_over_time(kw, cat='', timeframe='today 12-m', geo='BR', gprop='')
    data_dict['df_it'].append(data_it)

"""
for kw in keywords_list:
    data_it, data_ir, data_rt, data_rq = gt.check_trends(kw,'today 12-m', 'BR', 'COUNTRY', False, True)
    data_dict['df_it'].append(data_it)
    data_dict['df_ir'].append(data_ir)
    data_dict['df_rt'].append(data_rt)
    data_dict['df_rq'].append(data_rq)
""" 

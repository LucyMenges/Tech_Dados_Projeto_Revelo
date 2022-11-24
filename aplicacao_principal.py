# -*- coding: utf-8 -*-

import gt_script as gt

keywords_list = ['SQL', 'Python',
                 'Power BI', 'Pandas']

data_dict = {'keywords': keywords_list, 'df_it': [],
             'df_ir': [], 'df_rt': [], 'df_rq': []}

for kw in keywords_list:
    data_it, data_ir, data_rt, data_rq = gt.check_trends(
        kw, cat='0', timeframe='today 12-m', geo='BR', gprop='',
        resolution='COUNTRY', inc_low_vol=False, inc_geo_code=True)

    data_dict['df_it'].append(data_it)
    data_dict['df_ir'].append(data_ir)
    data_dict['df_rt'].append(data_rt)
    data_dict['df_rq'].append(data_rq)

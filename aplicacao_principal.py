# -*- coding: utf-8 -*-
import gt_script as gt
import pandas as pd

keywords_list = ['SQL', 'Python']

data_dict = {'keywords': keywords_list, 'df_it': [],
             'df_ir': [], 'df_rt': []}

for kw in keywords_list:
    data_it, data_ir, data_rt = gt.check_trends(
        kw, cat='0', timeframe='today 12-m', geo='BR', gprop='',
        resolution='CITY', inc_low_vol=False, inc_geo_code=True)
    data_dict['df_it'].append(data_it)
    data_dict['df_ir'].append(data_ir)
    data_dict['df_rt'].append(data_rt)


i = 0
for kw1 in keywords_list:
    if i <= len(keywords_list):
        df = data_dict['df_it'][i]
        df.to_csv('data_it_' +str([kw1]), sep=',')  
        i =+ 1
    else:
        exit()


i = 0
for kw2 in keywords_list:
    if i <= len(keywords_list):
        df = data_dict['df_ir'][i]
        df.to_csv('df_ir_' +str([kw2]), sep=',')  
        i =+ 1
    else:
        exit()

i = 0
for kw3 in keywords_list:
    if i <= len(keywords_list):
        df = pd.DataFrame(data_dict['df_rt'][i][kw3]['top'])
        df.to_csv('df_rt_' +str([kw3]), sep=',')  
        i =+ 1
    else:
        exit()
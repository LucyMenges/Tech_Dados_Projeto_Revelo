# -*- coding: utf-8 -*-
import time
import gt_script as gt
import pandas as pd

keywords_list = ['SQL', 'Python',
                 'Power BI', 'Pandas']

data_dict = {'keywords': keywords_list, 'df_it': [],
             'df_ir': [], 'df_rt': []}

for kw in keywords_list:
    time.sleep(30)
    data_it, data_ir, data_rt = gt.check_trends(
        kw, cat='0', timeframe='today 12-m', geo='BR', gprop='',
        resolution='CITY', inc_low_vol=False, inc_geo_code=True)
    data_dict['df_it'].append(data_it)
    data_dict['df_ir'].append(data_ir)
    data_dict['df_rt'].append(data_rt)


# interest_over_time
df_it0 = pd.DataFrame(data_dict['df_it'][0])
df_it1 = pd.DataFrame(data_dict['df_it'][1])
df_it2 = pd.DataFrame(data_dict['df_it'][2])
df_it3 = pd.DataFrame(data_dict['df_it'][3])
# df_it4 = pd.DataFrame(data_dict['df_it'][4])
# df_it5 = pd.DataFrame(data_dict['df_it'][5])
# df_it6 = pd.DataFrame(data_dict['df_it'][6])
# df_it7 = pd.DataFrame(data_dict['df_it'][7])
# df_it8 = pd.DataFrame(data_dict['df_it'][8])
# df_it9 = pd.DataFrame(data_dict['df_it'][9])

# interest_by_region
df_ir0 = pd.DataFrame(data_dict['df_ir'][0])
df_ir1 = pd.DataFrame(data_dict['df_ir'][1])
df_ir2 = pd.DataFrame(data_dict['df_ir'][2])
df_ir3 = pd.DataFrame(data_dict['df_ir'][3])
# df_ir4 = pd.DataFrame(data_dict['df_ir'][4])
# df_ir5 = pd.DataFrame(data_dict['df_ir'][5])
# df_ir6 = pd.DataFrame(data_dict['df_ir'][6])
# df_ir7 = pd.DataFrame(data_dict['df_ir'][7])
# df_ir8 = pd.DataFrame(data_dict['df_ir'][8])
# df_ir9 = pd.DataFrame(data_dict['df_ir'][9])

# related_topics
df_rt0 = pd.DataFrame(data_dict['df_rt'][0]['SQL']['top'])
df_rt1 = pd.DataFrame(data_dict['df_rt'][1]['Python']['top'])
df_rt2 = pd.DataFrame(data_dict['df_rt'][2]['Power BI']['top'])
df_rt3 = pd.DataFrame(data_dict['df_rt'][3]['Pandas']['top'])
# df_rt4 = pd.DataFrame(data_dict['df_rt'][4]['']['top'])
# df_rt5 = pd.DataFrame(data_dict['df_rt'][5]['']['top'])
# df_rt6 = pd.DataFrame(data_dict['df_rt'][6]['']['top'])
# df_rt7 = pd.DataFrame(data_dict['df_rt'][7]['']['top'])
# df_rt8 = pd.DataFrame(data_dict['df_rt'][8]['']['top'])
# df_rt9 = pd.DataFrame(data_dict['df_rt'][9]['']['top'])
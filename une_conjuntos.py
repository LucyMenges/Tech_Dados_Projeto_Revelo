# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 11:37:08 2022

@author: Bruna Mulinari
"""
import pandas as pd
import numpy as np

diretorio = 'C:/_dev/residencia_harve/Tech_Dados_Projeto_Revelo/data_Habilidades/'

keywords_list = ['Inglês', 'Equipe', 'Responsável', 'Comunicação', 'Planejamento', 'Modelagem', 'Foco',
 'Estatística', 'Documentação', 'Inovação', 'Metodologias Ágeis', 'Decisão', 'Prazos', 'Extração de Dados', 
 'Machine Learning','Indicadores', 'Dashboards', 'Logística', 'Marketing', 'Implementação',  
 'ETL', 'Visão', 'Inteligência Artificial', 'Inteligência de Negócio', 'TI', 'Coleta de Dados', 'Fluxos']  

lista_data_ir = []
lista_data_it = []
lista_data_rt = []

for kw in keywords_list:
    
    df_ir = pd.read_csv(diretorio + 'data_ir_' +str([kw]), sep=',')
    df_ir['habilidades'] = np.repeat(df_ir.columns[2], df_ir.shape[0]) 
    df_ir.columns = ['geoname', 'geocode', 'quantidade', 'habilidades']
    lista_data_ir.append(df_ir)
    
    df_it = pd.read_csv(diretorio + 'data_it_' +str([kw]), sep=',')
    df_it['habilidades'] = np.repeat(df_it.columns[1], df_it.shape[0]) 
    df_it.columns = ['date', 'quantidade', 'isPartial', 'habilidades']
    lista_data_it.append(df_it)
    
    df_rt = pd.read_csv(diretorio + 'data_rt_' +str([kw]), sep=',')
    df_rt['habilidades'] = np.repeat(kw, df_rt.shape[0])
    lista_data_rt.append(df_rt)
    
    
df_ir_total = pd.concat(lista_data_ir, axis = 0)
df_ir_total.to_csv('df_ir_total_hab.csv')
df_it_total = pd.concat(lista_data_it, axis = 0)
df_it_total.to_csv('df_it_total_hab.csv')
df_rt_total = pd.concat(lista_data_rt, axis = 0)
df_rt_total.to_csv('df_rt_total_hab.csv')
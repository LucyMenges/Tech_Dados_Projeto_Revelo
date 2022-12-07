# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 11:37:08 2022

@author: Bruna Mulinari
"""
import pandas as pd
import numpy as np

diretorio = 'C:/Users/llanz/OneDrive/Documents/GitHub/Tech_Dados_Projeto_Revelo/data_Ferramentas/'

keywords_list = ['Excel', 'Power BI',  'Banco de Dados', 'Pacote Office',
                 'SQL', 'SAP', 'Python', 'Cloud', 'CRM', 'Protheus', 'Analytics',
                 'Oracle', 'R', 'Azure', 'Salesforce', 'Linux']  


lista_data_ir = []
lista_data_it = []
lista_data_rt = []

for kw in keywords_list:
    
    df_ir = pd.read_csv(diretorio + 'data_ir_' +str([kw]), sep=',')
    df_ir['ferramenta'] = np.repeat(df_ir.columns[2], df_ir.shape[0]) 
    df_ir.columns = ['geoname', 'geocode', 'quantidade', 'ferramenta']
    lista_data_ir.append(df_ir)
    
    df_it = pd.read_csv(diretorio + 'data_it_' +str([kw]), sep=',')
    df_it['ferramenta'] = np.repeat(df_it.columns[1], df_it.shape[0]) 
    df_it.columns = ['date', 'quantidade', 'isPartial', 'ferramenta']
    lista_data_it.append(df_it)
    
    df_rt = pd.read_csv(diretorio + 'data_rt_' +str([kw]), sep=',')
    df_rt['ferramenta'] = np.repeat(kw, df_rt.shape[0])
    lista_data_rt.append(df_rt)
    
    
df_ir_total = pd.concat(lista_data_ir, axis = 0)
df_ir_total.to_csv('df_ir_total.csv')
df_it_total = pd.concat(lista_data_it, axis = 0)
df_it_total.to_csv('df_it_total.csv')
df_rt_total = pd.concat(lista_data_rt, axis = 0)
df_rt_total.to_csv('df_rt_total.csv')
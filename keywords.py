# import ws_script as ws

# # PARAMETROS 
# # Criar o navegador, com o google Chrome atualizado.
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# servico = Service(ChromeDriverManager().install())
# nav = webdriver.Chrome(service=servico)
# nav.set_page_load_timeout(300)

# # Link da página a ser aberta pelo navegador
# pag1 = "https://www.vagas.com.br/"

# # Cargo a ser pesquisado
# cargos = ['Analista de Dados']

# nr_pag = 2

# # Transformando o resultado num DataFrame
# df3 =  ws.busca_site_vagas(nav, pag1, cargos, nr_pag=2)

# # Salvando o dataFrame final para CSV file
# df3.to_csv("lista2_vagas_vagas_com.csv")

import pandas as pd
import nltk
import re
import string
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize

# UNINDO TODOS OS DF DE CADA LINK

lista_df = []

for i in range(120):  
    
    if (not(i in [31,68, 90, 113])):  
    
        df = pd.read_csv('Informacoes_' + str(i) + '.csv')
        lista_df.append(df)

df_total = pd.concat(lista_df)

df_total.to_csv('df_total_descr.csv')

df_total = pd.read_csv(r'C:\Users\Engenharia R3\Documents\GitHub\Tech_Dados_Projeto_Revelo\df_total_descr.csv') 
df_total = df_total.astype(str)

stop_words = stopwords.words('portuguese')

removal_words = ['descrição', 'conhecimento', 'experiência', 'requisitos', 'área', 'outros', 'atividades', 'nível', 'áreas', 'desejável', 'informações', 'realizar', 'completo', 'empresa','através','fazer','principais','·','vida', '–','bem','novos','aqui','eou','time',]

def cleaning(text):   
    # Converter para letra minúscula, Remover links URL, caracteres especiais, pontuações...
    text = text.lower()
    text = re.sub('https?://S+|www.S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('/n','', text)
    text = re.sub('[’“”…]', '', text)
    text = re.sub('•','', text)

    for word in removal_words:
     text = re.sub(word,'', text) 


    # Remover emojis (não será necessário) 
    # emoji_pattern = re.compile("["
    #                        u"U0001F600-U0001F64F"  # emoticons
    #                        u"U0001F300-U0001F5FF"  # symbols & pictographs
    #                        u"U0001F680-U0001F6FF"  # transport & map symbols
    #                        u"U0001F1E0-U0001F1FF"  # flags (iOS)
    #                        u"U00002702-U000027B0"
    #                        u"U000024C2-U0001F251"
    #                        "]+", flags=re.UNICODE)
    # text = emoji_pattern.sub(r'', text)   
    
    # Remover stop-words         
    text_tokens = word_tokenize(text)
    tokens_without_sw = [word for word in text_tokens if not word in stop_words]
    filtered_sentence = (" ").join(tokens_without_sw)
    text = filtered_sentence
    
    return text

# Filtrar as linhas que contém a string 'descrição:' 
df_total.loc[df_total['descr2_vg'].str.contains('descrição:', case=False, na=False), "descrição_final"] =  df_total['descr2_vg']
df_total.loc[df_total['descr3_vg'].str.contains('descrição:', case=False, na=False), "descrição_final"] =  df_total['descr3_vg']

# Aplicar a função para limpar/filtrar as strings
dt1 = df_total['descrição_final'].apply(cleaning)

# Contar as palavras que mais aparecem na coluna "descrição_final"
from collections import Counter
p1 = Counter(" ".join(dt1).split()).most_common(500)

rslt = pd.DataFrame(p1, columns=['Word', 'Frequency'])
print(rslt)

# Salvando o dataFrame final para CSV file
rslt.to_csv("rslt1.csv")
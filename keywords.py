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


# Contando palavras que mais aparecem no dataframe
# print(lista_vagas_vagas_com.titulo.str.split(expand=True).stack().value_counts())

import pandas as pd
import nltk
import re
import string
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize


lista_vagas_vagas_com = pd.read_csv(r'C:\Users\Engenharia R3\Documents\GitHub\Tech_Dados_Projeto_Revelo\lista2_vagas_vagas_com.csv')
lista_vagas_vagas_com=lista_vagas_vagas_com.astype(str)

stop_words = stopwords.words('portuguese')

def cleaning(text):        
    # Converter para letra minúscula, Remover links URL, caracteres especiais, pontuações...
    text = text.lower()
    text = re.sub('https?://S+|www.S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('/n','', text)
    text = re.sub('[’“”…]', '', text)     

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
lista_vagas_vagas_com.loc[lista_vagas_vagas_com['descrição2_vg'].str.contains('descrição:', case=False, na=False), "descrição_final"] =  lista_vagas_vagas_com['descrição2_vg']
lista_vagas_vagas_com.loc[lista_vagas_vagas_com['descrição3_vg'].str.contains('descrição:', case=False, na=False), "descrição_final"] =  lista_vagas_vagas_com['descrição3_vg']

# Aplicar a função para limpar/filtrar as strings
dt1 = lista_vagas_vagas_com['descrição_final'].apply(cleaning)


from collections import Counter
p1 = Counter(" ".join(dt1).split()).most_common(30)

rslt = pd.DataFrame(p1, columns=['Word', 'Frequency'])
print(rslt)
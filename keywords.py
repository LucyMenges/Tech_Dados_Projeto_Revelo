# -*- coding: utf-8 -*-
# @author: Wilsner Sakimoto

# IMPORTAÇÃO DE BIBLIOTECAS
import pandas as pd
import nltk
import re
import string
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from collections import Counter

# UNIÃO DE TODOS OS DATAFRAMES DE CADA LINK
lista_df = []

for i in range(120):  
    
    if (not(i in [31,68, 90, 113])):  
    
        df = pd.read_csv('Informacoes_' + str(i) + '.csv')
        lista_df.append(df)

df_total = pd.concat(lista_df)
df_total.to_csv('df_total_descr.csv')
df_total = pd.read_csv(r'C:\Users\Engenharia R3\Documents\GitHub\Tech_Dados_Projeto_Revelo\df_total_descr.csv') 
df_total = df_total.astype(str)

# SEPARAÇÃO DAS STOP-WORDS E PRÉ-SELEÇÃO DE PALAVRAS A REMOVER DO DATAFRAME GERADO
stop_words = stopwords.words('portuguese')
removal_words = ['descrição', 'conhecimento', 'experiência', 'requisitos', 'área', 'outros', 'atividades', 'nível', 'áreas', 'desejável', 'informações', 'realizar', 'completo', 'empresa','através','fazer','principais','·','vida', '–','bem','novos','aqui','eou','time',]

# FUNÇÃO PARA FAZER A LIMPEZA GERAL DA STRING NA COLUNA DE DESCRIÇÕES DAS VAGAS
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

    # # Remover emojis (não será necessário) 
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

# FILTRAR AS LINHAS QUE CONTÉM A STRING 'DESCRIÇÃO:' E ADICIONANDO EM UMA TERCEIRA COLUNA 
df_total.loc[df_total['descr2_vg'].str.contains('descrição:', case=False, na=False), "descrição_final"] =  df_total['descr2_vg']
df_total.loc[df_total['descr3_vg'].str.contains('descrição:', case=False, na=False), "descrição_final"] =  df_total['descr3_vg']

# APLICAR A FUNÇÃO PARA LIMPEZA/FILTRO DAS STRINGS
dt1 = df_total['descrição_final'].apply(cleaning)

# CONTAGEM DE PALAVRAS QUE MAIS APARECEM NA COLUNA 'DESCRIÇÃO_FINAL'
p1 = Counter(" ".join(dt1).split()).most_common(500)
rslt = pd.DataFrame(p1, columns=['Word', 'Frequency'])
print(rslt)

# SALVAR O DATAFRAME FINAL PARA CSV FILE
rslt.to_csv("rslt1.csv")
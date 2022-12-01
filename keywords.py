import ws_script as ws

# Criar o navegador, com o google Chrome atualizado.
nav = webdriver.Chrome(service=servico)

# Link da página a ser aberta pelo navegador
pag1 = "https://www.vagas.com.br/"

# Cargo a ser pesquisado
cargos = ['Analista de Dados']

nr_pag = 2

# Transformando o resultado num DataFrame
df3 =  ws.busca_site_vagas(nav, pag1, cargos, nr_pag=2)

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


lista_vagas_vagas_com = pd.read_csv(r'C:\Users\Engenharia R3\Documents\GitHub\Tech_Dados_Projeto_Revelo\lista_vagas_vagas_com.csv')
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

# Aplicar a função para limpar/filtrar as strings
dt1 = lista_vagas_vagas_com['descrição_vg'].apply(cleaning)

# dt2 = lista_vagas_vagas_com['desc_empresa_vg'].apply(cleaning)

from collections import Counter
p1 = Counter(" ".join(dt1).split()).most_common()
# p2 = Counter(" ".join(dt2).split()).most_common(10)
rslt1 = pd.DataFrame(p1, columns=['Word', 'Frequency'])
print(rslt1)
# rslt2 = pd.DataFrame(p2, columns=['Word', 'Frequency'])
# print(rslt2)

# rslt1.to_csv("rslt1.csv")
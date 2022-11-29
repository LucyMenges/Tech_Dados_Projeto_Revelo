# PROJETO 3 RESIDENCIA TECH - REVELO

# Created on Tue Nov 15 17:57:48 2022
# @authors: Luciana Lanzoni Menges e Rafael Cespedes
# -*- coding: utf-8 -*-

# Projeto:
    #Coletar informações em determinado site e criar associação com API e gerar resultado para análise.
    
# Estrutura do Projeto
    # 1. Web Scraping
        ## Vamos criar uma automação web usando o selenium, para rodar o Goggle Chrome em 1º plano
    
    # 2. Conexão com API
    
# Pré-requisitos para execução do script, aqui faremos apenas o indicação dos itens a serem instalados, caso não os tenha já instalados.
    
    # Instalação do selenium
         # Para a instalar a biblioteca do Selenium abra o prompt do anaconda e execute o comando:
             # pip install --upgrade selenium
             
    # Instalação do webdriver # Importante!!!
        # Depois execute o seguinte comando para instalar o webdriver-manager:
            # pip install webdriver-manager
            
            # Vamos usar o webdriver-manager, uma outra biblioteca que faz o gerenciamento do chromedriver para você. 
            # Em seguida, importamos o ChromeDriverManager e usamos ele no Serviço do nosso Selenium,
            # Ou seja, faremos a atualização do webdriver de acordo com a versão que está no seu computados do Google Chrome.
    
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

servico = Service(ChromeDriverManager().install())
    
    
# Referências :
# https://selenium-python.readthedocs.io/index.html
# curso Python, https://www.hashtagtreinamentos.com/


# 1. Web Scraping site de vagas de emprego

## Sites para busca:    
### https://www.vagas.com.br/
### https://br.indeed.com/


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Bibliotecas utilizadas:
import pandas as pd
        
# Função para busca de informações no site indicado
def busca_site_vagas(nav, pag1, cargos):

    # Abrindo a página selecionada no navegador.
    nav.get(pag1)
    # nav2.get(pag2)

    # buscar vagas para o cargo indicado
    nav.find_element(By.XPATH,'/html/body/header/section/div/form/input').send_keys(cargos)
    nav.find_element(By.XPATH,'/html/body/header/section/div/form/input').send_keys(Keys.ENTER)

    # Tempo de espera de 20 segundos para conclusão ou até mostrar todas classes 'cargo'
    wait = WebDriverWait (nav, 20)
    element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cargo')))
    
    # pega o resultado da busca no site
    lista_geral = nav.find_elements(By.CLASS_NAME,'informacoes-header')

    # para cada anúncio na primeira página, pegará as seguintes informações: 
        #  id, título, nome empresa, nível e link da vaga 
    # Informações retiradas da classe do cabeçalho do anúncio.  

    lista_vagas = []  #lista que a função dará como resposta

    for anuncio in lista_geral:
        id_vg = anuncio.find_element(By.CLASS_NAME, 'link-detalhes-vaga').get_attribute('id')
        tit_vg = anuncio.find_element(By.CLASS_NAME, 'cargo').text
        empresa = anuncio.find_element(By.CLASS_NAME, 'emprVaga').text
        nivel_vg = anuncio.find_element(By.CLASS_NAME, 'nivelVaga').text
        link_vg = anuncio.find_element(By.CLASS_NAME, 'link-detalhes-vaga').get_attribute('href')
        lista_vagas.append((id_vg, tit_vg, empresa, nivel_vg, link_vg))
    return lista_vagas


# Criar o navegador, com o google Chrome atualizado.
nav = webdriver.Chrome(service=servico)

# Link da página a ser aberta pelo navegador
pag1 = "https://www.vagas.com.br/"
#pag2 = "https://br.indeed.com/"

# Cargo a ser pesquisado
cargos = ['Analista de Dados']

lista_vagas_vagas_com = pd.DataFrame((busca_site_vagas (nav, pag1, cargos)), columns=['id', 'titulo',  'empresa', 'nivel_da_vaga', 'link'])
print (lista_vagas_vagas_com)

# Contando palavras que mais aparecem na coluna "titulo"
# print(lista_vagas_vagas_com.titulo.str.split(expand=True).stack().value_counts())

import re
import string
import nltk

from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

STOP_WORDS = stopwords.words('portuguese')

def cleaning(text):
    """
    Converter texto para minúsculo.
    Remover links de URL, caracteres especiais e pontuações.
    Tokenizar o texto e remover stop words em português.
    """
    text = text.lower()
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('[’“”…]', '', text)

    # Remover stop-words
    text_tokens = word_tokenize(text)
    tokens_without_sw = [
        word for word in text_tokens if not word in STOP_WORDS]
    filtered_sentence = (" ").join(tokens_without_sw)
    text = filtered_sentence

    return text


if __name__ == "__main__":
    
    dt = lista_vagas_vagas_com['titulo'].apply(cleaning)

    word_count = Counter(" ".join(dt).split()).most_common(10)
    word_frequency = pd.DataFrame(word_count, columns = ['Word', 'Frequency'])
    print(word_frequency)
# PROJETO 3 RESIDENCIA TECH - REVELO

# Created on Tue Nov 15 17:57:48 2022
# @authors: Luciana Lanzoni Menges e Rafael Cespedes
# -*- coding: utf-8 -*-

# Projeto:
    #Coletar informações em determinado site e criar associação com API e gerar resultado para análise.
    
# Estrutura do Projeto
    # 1. Web Scraping
    # 2. Conexão com API
    
## 1. Web Scraping site de vagas de emprego

## Sites para busca:    
### https://www.vagas.com.br/
### https://br.indeed.com/

# Vamos criar uma automação web usando o selenium, para rodar o Goggle Chrome em 1º plano
# Importante: baixar o webdriver.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Bibliotecas utilizadas:
import pandas as pd
        
# Link da página a ser aberta pelo navegador
pag1 = "https://www.vagas.com.br/"
#pag2 = "https://br.indeed.com/"

# Abrindo a página selecionada num navegador novo.
nav = webdriver.Chrome()
nav.get(pag1)

# nav2 = webdriver.Chrome()
# nav2.get(pag2)

cargos = ['Analista de Dados']

# pesquisar vagas para "Analista de Dados"
nav.find_element(By.XPATH,'/html/body/header/section/div/form/input').send_keys(cargos)
nav.find_element(By.XPATH,'/html/body/header/section/div/form/input').send_keys(Keys.ENTER)


# Criando uma lista com as informações (id, título, nome empresa, nível e link da vaga) dos anúncios na primeira página geral
# Informações retiradas da classe do cabeçalho do anúncio.

lista_vagas = []

lista_geral = nav.find_elements(By.CLASS_NAME,'informacoes-header')

for resultado in lista_geral:
    id_vg = resultado.find_element(By.CLASS_NAME, 'link-detalhes-vaga').get_attribute('id')
    tit_vg = resultado.find_element(By.CLASS_NAME, 'cargo').text
    empresa = resultado.find_element(By.CLASS_NAME, 'emprVaga').text
    nivel_vg = resultado.find_element(By.CLASS_NAME, 'nivelVaga').text
    link_vg = resultado.find_element(By.CLASS_NAME, 'link-detalhes-vaga').get_attribute('href')
    lista_vagas.append((id_vg, tit_vg, empresa, nivel_vg, link_vg))

# Colocando a lista num dataFrame.

df = pd.DataFrame(lista_vagas, columns=['id', 'titulo',  'empresa', 'nivel_da_vaga', 'link'])
print (df)







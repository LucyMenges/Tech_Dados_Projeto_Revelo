# -*- coding: utf-8 -*-

## @package ws_script 

# PROJETO 3 RESIDENCIA TECH - REVELO

# Created on Tue Nov 15 17:57:48 2022
# @authors: Residencia Tech Analista Dados - Luciana Lanzoni Menges

# Referências :
# https://selenium-python.readthedocs.io/index.html
# curso Python, https://www.hashtagtreinamentos.com/

# Pré-requisitos para execução do script:
    # Instalação do selenium
    # Instalação do webdriver_manager
    
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

servico = Service(ChromeDriverManager().install())
    
# Bibliotecas utilizadas do Selenium:
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Outras Bibliotecas utilizadas:
import pandas as pd
import time 
import numpy as np

## 1. Web Scraping site de vagas de emprego para busca:
# https://www.vagas.com.br/

## busca_site_vagas
# Função que buscará determinadas informações no site indicado.

# @param nav: str, navegador do Google Chrome
# @param pag1: str, endereço do site para a busca
# @param cargos: str, nome do cargo a ser buscado
# @param nr_pag: int, quantidade de páginas, que serão abertas para a consulta, caso não indicado outro valor serão abertas duas páginas.

def busca_site_vagas(pag1, cargos, nr_pag=2):

    # Abrindo a página selecionada no navegador.
    nav = webdriver.Chrome(service=servico)
    nav.set_page_load_timeout(10)
    nav.get(pag1)

    # preenche com o nome do cargo indicado, no campo para pesquisa.
    nav.find_element(By.XPATH,'/html/body/header/section/div/form/input').send_keys(cargos)
    nav.find_element(By.XPATH,'/html/body/header/section/div/form/input').send_keys(Keys.ENTER)

    # Tempo de espera de 20 segundos para conclusão ou até mostrar todas classes 'cargo' do html.
    wait = WebDriverWait (nav, 20)
    element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cargo')))
    
    # Processo para mostrar mais vagas, clica o nr_pag indicado, "abrir nova página".
    j=0
    while (j < nr_pag):
        try:
            nav.find_element(By.CSS_SELECTOR, '#maisVagas').send_keys(Keys.ENTER)
            time.sleep(2)  # segundos
            j = j+1
        except:
            break
    
    # marca o cabeçalho de cada anuncio do resultado da busca.
    lista_geral = nav.find_elements(By.CLASS_NAME,'informacoes-header')

    lista_vagas = []  #lista que a função dará como resposta
    
    # para cada anúncio da página completa, pegará as seguintes informações:
        #  id, título, nome empresa, nível e link da vaga 

    for anuncio in lista_geral:
        id_vg = anuncio.find_element(By.CLASS_NAME, 'link-detalhes-vaga').get_attribute('id')
        tit_vg = anuncio.find_element(By.CLASS_NAME, 'cargo').text
        empresa = anuncio.find_element(By.CLASS_NAME, 'emprVaga').text
        nivel_vg = anuncio.find_element(By.CLASS_NAME, 'nivelVaga').text
        link_vg = anuncio.find_element(By.CLASS_NAME, 'link-detalhes-vaga').get_attribute('href')
        lista_vagas.append((id_vg, tit_vg, empresa, nivel_vg, link_vg))
        
    lista_vagas_vagas_com = pd.DataFrame(lista_vagas, columns=['id', 'titulo',  'empresa', 'nivel_da_vaga', 'link'])
    print (len(lista_vagas_vagas_com))
    lista_vagas_vagas_com.to_csv('Lista_geral_links.csv')
    
    nav.close()
    
    return lista_vagas_vagas_com

# SEGUNDA FUNÇAO

def busca_descr_link (url):
    
    lista2 = []
    
    # Abre a página selecionada neste navegador
    nav = webdriver.Chrome(service=servico)
    nav.set_page_load_timeout(10)
    nav.get(url)
    
    # Tempo de espera de 20 segundos para conclusão ou até mostrar todas classes de informações
    wait = WebDriverWait (nav, 20)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section[2]/main/article/div[3]')))
    
    # Informações a serem armazenadas:
    # data publicação
    data_publi = nav.find_element(By.XPATH, '//*[@id="wrapper-pesquisas"]/section[1]/div/div[1]/ul/li[1]').text
    
    # salario
    salario_vg = nav.find_element(By.XPATH, '//*[@id="JobContent"]/article/header/div/ul/li[1]/div/span[2]').text
    
    # localização
    cidade_vg = nav.find_element(By.CLASS_NAME, 'info-localizacao').text
    
    # descrição
    descr3_vg = nav.find_element(By.XPATH, '//*[@id="JobContent"]/article/div[3]').text
    
    # descrição da empresa
    descr2_vg = nav.find_element(By.XPATH, '//*[@id="JobContent"]/article/div[2]').text
    
    lista2.append((data_publi, salario_vg, cidade_vg, descr3_vg, descr2_vg ))
    
    lista2 = pd.DataFrame(np.reshape(lista2, (1, 5)), columns = ['data_publi', 'salario_vg', 'cidade_vg', 'descr3_vg', 'descr2_vg'])
    
    return lista2

# PRIMEIRO vai ter salvo o df relacionado ao link das vagas

# Link da página a ser aberta pelo navegador
pag1 = "https://www.vagas.com.br/"

# Cargo a ser pesquisado
cargos = ['Analista de Dados']

# Qtidade de páginas a serem abertas
nr_pag = 2

# Transformando o resultado num DataFrame
df3 =  busca_site_vagas( pag1, cargos, nr_pag=2)
print(df3)

# CHAMANDO A SEGUNDA FUNÇÃO

df3 = pd.read_csv('Lista_geral_links.csv')

for i, url in enumerate(df3['link']):
    
    if (i < 60):   # depois muda para >60
        df_desc = busca_descr_link(url)
        
        df1 = pd.DataFrame(np.reshape(list(df3.iloc[i,:]), (1, 6)), columns = ['index', 'id', 'titulo', 'empresa', 'nivel_da_vaga', 'link'])
        
        df_total = pd.concat([df1, df_desc], axis= 1)
        df_total.to_csv('Informacoes_' + str(i) + '.csv')
        
    print(i)
    
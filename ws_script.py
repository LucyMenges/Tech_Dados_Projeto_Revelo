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

## 1. Web Scraping site de vagas de emprego para busca:
# https://www.vagas.com.br/

## busca_site_vagas
# Função que buscará determinadas informações no site indicado.

# @param nav: str, navegador do Google Chrome
# @param pag1: str, endereço do site para a busca
# @param cargos: str, nome do cargo a ser buscado
# @param nr_pag: int, quantidade de páginas, que serão abertas para a consulta, caso não indicado outro valor serão abertas duas páginas.

def busca_site_vagas(nav, pag1, cargos, nr_pag=2):

    # Abrindo a página selecionada no navegador.
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
            time.sleep(2)
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
    
    # Segunda fase
    lista_vagas2 = []
    
    for elemento in lista_vagas_vagas_com['link']:
        
        # Abre a página selecionada neste navegador
        nav.get(elemento)
        
        # Tempo de espera de 10 segundos para conclusão ou até mostrar todas classes de informações
        wait = WebDriverWait (nav, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section[2]/main/article/div[3]')))
        
        # Informações a serem armazenadas:
        # data publicação
        data_publi = nav.find_element(By.XPATH, '//*[@id="wrapper-pesquisas"]/section[1]/div/div[1]/ul/li[1]').text
        
        # salario
        salario_vg = nav.find_element(By.XPATH, '//*[@id="JobContent"]/article/header/div/ul/li[1]/div/span[2]').text
        
        # localização
        cidade_vg = nav.find_element(By.CLASS_NAME, 'info-localizacao').text
        
        # descrição
        descri_vg = nav.find_element(By.XPATH, '//*[@id="JobContent"]/article/div[3]').text
        
        # descrição da empresa
        desc_empr_vg = nav.find_element(By.XPATH, '//*[@id="JobContent"]/article/div[2]').text
        
     
        lista_vagas2.append((data_publi, salario_vg, cidade_vg, descri_vg, desc_empr_vg ))
        
    lista_vagas_vagas_com2 = pd.DataFrame(lista_vagas2, columns=['data_publicação', 'salario_vg', 'cidade_vg', 'descrição_vg', 'desc_empresa_vg'])
    
    todas_vagas = lista_vagas_vagas_com.join(lista_vagas_vagas_com2)
       
    return lista_vagas_vagas_com, lista_vagas_vagas_com2, todas_vagas

# -------------------
# Wil - APLICAÇÃO

# PARAMETROS 
# Criar o navegador, com o google Chrome atualizado.
nav = webdriver.Chrome(service=servico)

# Link da página a ser aberta pelo navegador
pag1 = "https://www.vagas.com.br/"

# Cargo a ser pesquisado
cargos = ['Analista de Dados']

nr_pag = 2

# Transformando o resultado num DataFrame
df1, df2, df3 =  busca_site_vagas(nav, pag1, cargos)

print (df3)
# Salvando o primeiro dataFrame para CSV file
df1.to_csv("lista1_vagas_vagas_com"+"data"+".csv")

# Salvando o dataFrame final para CSV file
df3.to_csv("lista2_vagas_vagas_com.csv")
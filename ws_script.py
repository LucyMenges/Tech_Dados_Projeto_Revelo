# PROJETO 3 RESIDENCIA TECH - REVELO

# Created on Tue Nov 15 17:57:48 2022
# @authors: Luciana Lanzoni Menges e Rafael Cespedes

# Projeto:
    #Coletar informações em determinado site e criar associação com API e gerar resultado para análise.
    
# Estrutura do Projeto
    # 1. Web Scraping
    # 2. Conexão com API
    
## 1. Web Scraping site de vagas de emprego

## Sites para busca:    
### https://www.vagas.com.br/
### https://br.indeed.com/

# -*- coding: utf-8 -*-

# Vamos criar uma automação web usando o selenium, para rodar o Goggle Chrome em 1º plano
# Importante: baixar o webdriver.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

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


# Pegar as informações (id, título e link da vaga) dos anúncios na primeira página geral

lista_titulos_vg = nav.find_elements(By.CLASS_NAME, 'cargo')
for elemento_titulo in lista_titulos_vg:
    titulo_vg = elemento_titulo.text
    print(titulo_vg)
    

# pegando informações na pagina de anúncios
# nome da vaga 
header_vg = nav.find_element(By.CLASS_NAME, 'informacoes-header').text
print (header_vg)


# pegando informações na pagina de anúncios
# nome da vaga 
titulo_vg = nav.find_element(By.CLASS_NAME, 'cargo').text
print (titulo_vg)

link_vg = nav.find_element(By.CLASS_NAME, 'link-detalhes-vaga').get_attribute('href')
print(link_vg)


# abrir primeiro anúncio da página
nav.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/section/section/div/ul/li[1]/header/div[2]/h2/a').send_keys(Keys.ENTER)

# Criando o dicionário para armazenar as informações
vaga1 = {'data_publi' : [], 'titulo_vg' : [], 'empresa' : [], 'salario' : [], 'cidade_vg' : [], 'job_desc' : []}

# pegar as informaçãoes necessárias:

# Data da publicação do anúncio
data_publi = nav.find_element(By.XPATH, '//*[@id="wrapper-pesquisas"]/section[1]/div/div[1]/ul/li[1]').text
print (data_publi)

# título da vaga
titulo_vg2 = nav.find_element(By.CLASS_NAME, 'job-shortdescription__title').text
print (titulo_vg2)

#nome empresa
empresa = nav.find_element(By.CLASS_NAME, 'job-shortdescription__company').text
print (empresa)

# faixa salarial
salario = nav.find_element(By.XPATH, '//*[@id="JobContent"]/article/header/div/ul/li[1]/div').text
print(salario)

# localização
cidade_vg = nav.find_element(By.CLASS_NAME, 'info-localizacao').text
print (cidade_vg)

# job description
job_desc = nav.find_element(By.XPATH, '//*[@id="JobContent"]/article/div[3]').text
#job_desc = nav.find_element(By.CLASS_NAME, 'job-tab-content job-description__text texto').text
# não encontrou pela classe
print (job_desc)




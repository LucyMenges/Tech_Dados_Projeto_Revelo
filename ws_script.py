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

# Bibliotecas utilizadas do Selenium:
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Outras Bibliotecas utilizadas:
import pandas as pd
import time 
      
# Função para buscar determinadas informações no site indicado

# @param nav: str, navegador do Google Chrome
# @param pag1: str, endereço do site para a busca
# @param cargos: str, nome do cargo a ser buscado

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
    
    # Processo para mostrar mais vagas, "abrir nova página".
    j=0
    while (j < 2):
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
        #(retiradas da classe do cabeçalho do anúncio)
        #  id, título, nome empresa, nível e link da vaga 

    for anuncio in lista_geral:
        id_vg = anuncio.find_element(By.CLASS_NAME, 'link-detalhes-vaga').get_attribute('id')
        tit_vg = anuncio.find_element(By.CLASS_NAME, 'cargo').text
        empresa = anuncio.find_element(By.CLASS_NAME, 'emprVaga').text
        nivel_vg = anuncio.find_element(By.CLASS_NAME, 'nivelVaga').text
        link_vg = anuncio.find_element(By.CLASS_NAME, 'link-detalhes-vaga').get_attribute('href')
        lista_vagas.append((id_vg, tit_vg, empresa, nivel_vg, link_vg))
    return lista_vagas

# VARIÁVEIS
# Criar o navegador, com o google Chrome atualizado.
nav = webdriver.Chrome(service=servico)

# Link da página a ser aberta pelo navegador
pag1 = "https://www.vagas.com.br/"
#pag2 = "https://br.indeed.com/"

# Cargo a ser pesquisado
cargos = ['Analista de Dados']

# Transformando o resultado em um DataFrame
lista_vagas_vagas_com = pd.DataFrame((busca_site_vagas (nav, pag1, cargos)), columns=['id', 'titulo',  'empresa', 'nivel_da_vaga', 'link'])
print (lista_vagas_vagas_com)

# Salvando o primeiro dataFrame para CSV file
lista_vagas_vagas_com.to_csv("lista1_vagas_vagas_com.csv")

# SEGUNDA PARTE 

# Para facilitar os testes está limitado a 45 links incialmente
# VALOR PODE SER ALTERADO. 
link_anuncio = lista_vagas_vagas_com['link'].head(45)


def detalhes_vagas (link_anuncio):

    lista_vagas2 = []
    
    for elemento in link_anuncio:
        # Abre a página selecionada neste navegador
        nav.get(elemento)
        
        # Tempo de espera de 10 segundos para conclusão ou até mostrar todas classes de informações
        wait = WebDriverWait (nav, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section[2]/main/article/div[3]')))
        
        # Informações a serem armazenadas
        # data publicação
        data_publi = nav.find_element(By.XPATH, '//*[@id="wrapper-pesquisas"]/section[1]/div/div[1]/ul/li[1]').text
        # descrição
        descri_vg = nav.find_element(By.XPATH, '//*[@id="JobContent"]/article/div[3]').text
        
        # descrição da empresa
        desc_empr_vg = nav.find_element(By.XPATH, '//*[@id="JobContent"]/article/div[2]').text
        
        # localização
        cidade_vg = nav.find_element(By.CLASS_NAME, 'info-localizacao').text
    
        lista_vagas2.append((data_publi, descri_vg, desc_empr_vg, cidade_vg))
        
    return lista_vagas2

# Transformando o resultado da função num segundo DataFrame
lista_vagas_vagas_com2 = pd.DataFrame((detalhes_vagas (link_anuncio)), columns=['data_publicação', 'descrição_vg', 'desc_empresa_vg', 'cidade_vg'])

# Unindo os dois dfs
lista_vagas_vagas_com = lista_vagas_vagas_com.join(lista_vagas_vagas_com2)
print(lista_vagas_vagas_com)

lista_vagas_vagas_com.info()

# Salvando o dataFrame final para CSV file
lista_vagas_vagas_com.to_csv("lista2_vagas_vagas_com.csv")



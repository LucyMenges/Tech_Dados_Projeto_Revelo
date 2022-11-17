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

nav = webdriver.Chrome()
nav.get("https://www.vagas.com.br/")

nav1 = webdriver.Chrome()
nav1.get("https://br.indeed.com/")
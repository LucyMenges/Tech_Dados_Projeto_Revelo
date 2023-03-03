# Tech_Dados
Serão desenvolvidos três projetos durante a Residencia Tech de Analise Dados, da Harve:

1. Projeto Olist (individual)
2. Projeto Setor Público (individual)
3. Projeto Revelo (grupo)


# Projeto 3 - Analise de Dados Revelo

**Desafio:**

A Revelo é uma referência em recrutamento de profissionais na área de tecnologia. 
Para continuar sendo destaque na área, ela precisa estar atenta aos movimentos do mercado de vagas e ferramentas. 
Aqui, você irá atuar em time, criar robôs em web scrapping para ler esses dados e criar associações com dados de apis e gerar apontamentos para onde a empresa precisa caminhar.
<br /><br />
**Grupo:**

* Luciana L Menges (linkedin.com/in/luciana-lanzoni-menges) 
* Raphael Céspedes (linkedin.com/in/rlccespedes)
* Wilsner Sakimoto (linkedin.com/in/wilsner) 
<br/><br/>
**Solução proposta pelo grupo:**

![image](https://user-images.githubusercontent.com/78648122/217348263-54218f42-c990-46c9-a10f-82fb628b56bc.png)

Os códigos foram desenvolvidos por:
* Luciana Menges - Fase 1
* Wilsner Sakimoto - Fase 2
* Raphael Céspedes - Fase 3  <br/>
A apresentação para a banca da Harve foi feita em conjunto, utilizando o Power BI para as visualizações, em dezembro/2022. Pode ser visto em: *Apresentaçao Detalhada Projeto 3.pdf*
<br /><br />
**Descrição do Github:**

**Arquivos:**
  * 00_Sprint Planing 3.pdf: backlog´s demandados pelo Product Owner e descrição dos sprints semanais.
  * ws_info.txt: Informações e esboço geral do projeto.
  * Apresentaçao Detalhada Projeto 3.pdf: Visualização detalhada dos dados resultantes após o Web scrapping e busca no Google Trends.
 <br /><br />

  * ws_script.py: Script com as duas funções criadas para o web scrapping no site de anúncio de vagas (Fase 1). Criado por Luciana Menges.
  * keywords.py: Script para filtrar e coletar as palavras-chave mais utilizadas nas descrições de vagas (Fase 2). Criado por Wilsner Sakimoto.
  * gt_script.py: Modulo para utilizar a lib PyTrends e agrupar metodos para analisar palavras-chave no Google Trends (Fase 3). Criado por Raphael Céspedes.
  * gt_app.py: Aplicação do módulo "gt_script.py" para as palavras selecionadas como Ferramentas e Habilidades (Fase 3). Criado por Raphael Céspedes.
  * une_conjuntos.py: Modulo para unir as listas das pastas "data_Habilidades" e "data_Ferramentas".<br /><br />

  * df_total_descr2.csv: Lista única com todas as informações das vagas salvas na pasta "Arquivos csv Detalhes Vaga"
  * rslt1.csv: Resultado da aplicação do código "keywords.py", lista com as palavras-chave mais utilizadas nas vagas salvas.
  * rslt1 - tratamento.xlsx: Análise e classificação das 500 palavras -chaves que mais apareceram na descrição das vagas.<br /><br />

  * df_ir_total_ferram.csv: Lista total das palavras-chave classificadas como Ferramentas, buscadas no Google Trends no "interesse por região".
  * df_ir_total_hab.csv: Lista total das palavras-chave classificadas como Habilidades, buscadas no Google Trends no "interesse por região".
  * df_it_total_ferram.csv: Lista total das palavras-chave classificadas como Ferramentas, buscadas no Google Trends no "interesse ao longo do tempo".
  * df_it_total_hab.csv: Lista total das palavras-chave classificadas como Habilidades, buscadas no Google Trends no "interesse ao longo do tempo".
  * df_rt_total_ferram.csv: Lista total das palavras-chave classificadas como Ferramentas, buscadas no Google Trends em "assuntos relacionados".
  * df_rt_total_hab.csv: Lista total das palavras-chave classificadas como Habilidades, buscadas no Google Trends em "assuntos relacionados".<br/><br/>
**Pastas:**
  * Arquivos csv Detalhes Vagas: Arquivos gerados na primeira parte do projeto, através do código "ws_script" (web scrapping). Cada arquivo corresponte a uma vaga anunciada no site, de acordo com os critérios selecionados. <br /><br />

  * data_Habilidades: Arquivos gerados na terceira parte do projeto, através da aplicação do código "gt_app.py"
  * data_Ferramentas: Arquivos gerados na terceira parte do projeto, através da aplicação do código "gt_app.py"<br /><br />

  * Documentation: Documentação do projeto gerada utilizando Doxygen.
  * Apresentação: arquivos utilizados para apresentação final à banca da Harve, em Power BI.<br/>
        * df_total_descr_Apresentacao.pbix: Visualização dos dados resultantes após o Web scrapping e busca no Google Trends.<br/>
        * Slides Apresentação Scrum Review 3.pdf: Slides da apresentação das conclusões do projeto.

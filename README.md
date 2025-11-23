# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Atividade Fase 4 Cap.03 

## Grupo 16

## 👨‍🎓 Integrantes: 
Roberto Ferreira da Silva Junior - RM: 561131

## 👩‍🏫 Professores:
### Tutor(a) 
- Sabrina Otoni
### Coordenador(a)
- André Godoi


## 📜 Descrição

Este repositório contém o notebook com o código da atividade do capítulo 3 - Fase 4 da FIAP. O código contém modelos de regressão em Machine Learning usados para prever dados do dataset Seeds. O desenvolvimento segue as etapas: pré-processamento, normalização de dados, treinamento de modelos, comparação de desempenho e avaliação de resultados.

## 📁 Arquivos principais

- atividade_cap3_fase4_FIAP_roberto_ferreira_rm561131.ipynb - Notebook da atividade
- seeds_dataset.txt - Dataset usado na atividade. Incluso para o carregamento correto dos dados no Notebook

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>src</b>: Código do projeto
    └── FASE4/
         └── CTWP/
              └── Cap3/
                  ├── atividade_cap3_fase4_FIAP_roberto_ferreira_rm561131.ipynb
                  └── seeds_dataset.txt

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 📊 Resultados e Conclusões
- O dataset Seeds é bem comportado, não exigindo maiores limpezas
- A normalização foi feita usando MinMaxScaler
- Modelos usados: KNN, SVC e Logistic Regression
- O KNN obteve os melhores resultados em todas as métricas e variedades.
  Curiosamente (ou não) usar k = 1 retornou os melhores resultados, apontando para uma forte separabilidade dos dados
- O kernel "poly" (degree=3) do SVC foi escolhido, pois retornava melhores precision e f1-score para a variedade "Kama"
  em relação aos kernel "rbf" e "linear", além de não apresentar grandes variações métricas para as outras variedades
- Entre os três modelos, o Logistic Regression apresentou as piores métricas para a variedade Kama, além da
  menor acurácia de todas (ainda que nenhuma das suas métricas tenha se apresentado baixíssima). Isso possivelmente
  nos mostra que um modelo que lide melhor com separações não-lineares dos dados talvez seja mais indicado para
  esse dataset


## 🔧 Como executar o código

- Clonar o repositório
- Abrir Jupyter Notebook ou Google Colab
- Executar as células na sequência em que aparecem


## 🗃 Histórico de lançamentos

* v1.0 - Atividade Fase 4 - Cap3

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>



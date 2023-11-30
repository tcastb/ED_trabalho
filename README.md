<h1 align="center">Trabalho de Estrutura de Dados</h1>

## Alunos
- **Lenardo de Lima Amaral**
  - **RA:** 22305363
  - **Curso:** Ciencias de Dados e Machine Learning
  - **E-mail:** leonardo.amaral90@live.com

- **Thiago Castro Barreto**
  - **RA:** 22301452
  - **Curso:** Ciencias de Dados e Machine Learning
  - **E-mail:** thiago.cb@sempreceub.com

## Dataset
O dataset utilizado neste trabalho foi localizado em [Kaggle](https://www.kaggle.com/datasets/shushant/data-science-job-dataset/).
- **Descrição:** Este conjunto de dados é a coleção de empregos relacionados à ciência de dados e analistas de dados. Ele é criado pela eliminação de postagens de emprego recentes de diferentes portais de empregos, como Even, Glassdoor e Linkedin.

## Estrutura do Projeto
- **model/:** Contém as classes e estruturas de dados utilizadas.
  - **Science.py:** Definição da classe `Science`.
  - **Node.py:** Definição da classe `Node`.
  - **BinaryNode.py:** Definição da classe `BinaryNode`.
  - **BinaryTree.py:** Definição da classe `BinaryTree`.
  - **ListaEncadeada.py:** Definição da classe `ListaEncadeada`.

- **main.ipynb:** Jupyter Notebook principal do projeto, contendo a implementação e análise.

## Execução do Projeto

### Pré-requisitos
Antes de começar, você vai precisar ter instalado em sua máquina a seguinte ferramenta:
[Git](https://git-scm.com). Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)

Para executar o projeto, siga os passos abaixo:

1. Clone este repositório:
   ```bash
   git clone https://github.com/tcastb/ED_trabalho.git
   cd ED_trabalho
   ```

## Instalação / Importação das bibliotecas
Utilizando sistema de gerenciador de pacotes.

Todos os pacotes utilizados na aplicação, é listado no arquivo 'requirements.txt'. 

É obrigatório a execução deste bloco de código antes de executar os demais blocos de códigos.
- %pip install -r requirements.txt
  - pandas==2.1.3 # https://pandas.pydata.org/docs/
  - matplotlib==3.8.1 # https://matplotlib.org/
  - seaborn==0.13.0 # https://seaborn.pydata.org/
  - numpy==1.26.2 # https://numpy.org/doc/
  - nbimporter==0.3.4 # https://github.com/grst/nbimporter
  - folium==0.15.0 # https://pypi.org/project/folium/
- import pandas as pd
- import matplotlib
- import matplotlib.pyplot as plt
- import seaborn
- import numpy as np
- import folium
- from folium.plugins import MarkerCluster

## Preparação de Dados
Atribuindo a variável 'principal' o arquivo .csv para tratabilidade.
 - df = pd.read_csv(r'data\data.csv', sep=',', encoding='utf-8')

Renomeando as colunas para uma melhor visualização.
 - df.columns = ['ID', 'Name', 'Company', 'Location', 'Description', 'Salary']

Verificado que a coluna em questão está para contagem de linhas, a mesma foi retirada do dataframe.
 - df.drop(['ID'], axis=1, inplace=True)

Fazendo a contagem de quantos NaN conta dentro da coluna 'Salary' para tratamento dentro da coluna.
 - df['Salary'].isna().sum()

Atribuindo 0 aos valores ausentes na coluna 'Salary'.
 - df['Salary'] = df['Salary'].fillna(0, inplace=False)

Função para tratar uma string dividida por vírgulas.

  def tratar_string(arg):
    
    partes = arg.split(',')
    
    if len(partes) == 1:   # Se houver apenas uma parte, converte para título (primeira letra de cada palavra maiúscula)
        return partes[0].title()
    elif len(partes) == 2: # Se houver duas partes, converte a primeira para título e a segunda para maiúsculas (removendo espaços em branco desnecessários)
        return f"{partes[0].title()}, {partes[1].strip().upper()}"
    elif len(partes) == 3: # Se houver três partes, converte a primeira para título, a segunda e a terceira para maiúsculas (removendo espaços em branco desnecessários)
        return f"{partes[0].title()}, {partes[1].strip().upper()}, {partes[2].strip().upper()}"
    else:                  # Se houver mais de três partes, retorna a string original
        return arg

Converte as colunas 'Name' e 'Company' para o formato de título

 df['Name'] = df['Name'].str.title()
 df['Company'] = df['Company'].str.title()
 df['Location'] = df['Location'].apply(tratar_string)  # Aplica a função tratar_string à coluna 'Location' do DataFrame
## Análise Utilizando Listas

## Análise Utilizando Árvores de Busca

## Análise Utilizando Grafos

## Visualização de Dados


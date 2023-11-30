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
[Git](https://git-scm.com).
Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)

Para executar o projeto, siga os passos abaixo:

1. Clone este repositório:
   ```bash
   git clone https://github.com/tcastb/ED_trabalho.git
   cd ED_trabalho
   ```

### 1.Instalação / Importação das bibliotecas
Utilizando sistema de gerenciador de pacotes.
Todos os pacotes utilizados na aplicação, é listado no arquivo 'requirements.txt'.
É obrigatório a execução deste bloco de código antes de executar os demais blocos de códigos.
*%pip install -r requirements.txt*
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn
import numpy as np
import folium
from folium.plugins import MarkerCluster

### 2.Preparação de Dados
- Atribuindo a variável 'principal' o arquivo .csv para tratabilidade
df = pd.read_csv(r'data\data.csv', sep=',', encoding='utf-8')
df.head()
- Renomeando as colunas para uma melhor visualização
df.columns = ['ID', 'Name', 'Company', 'Location', 'Description', 'Salary']
df.head()

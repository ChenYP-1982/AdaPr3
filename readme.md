
# Processo de Criação de um Banco de Dados e Desenvolvimento de Modelo de Machine Learning com Streamlit

Neste documento, discutiremos o processo de criação de um banco de dados, incluindo entendimento de atributos, entidades, cardinalidade, criação de tabelas e consultas para análise de dados. Posteriormente, abordaremos a exportação de dados para o desenvolvimento de modelos de machine learning e a criação de um modelo de deploy utilizando Streamlit.


Processo de Criação do Banco de Dados

1. Entendimento de Atributos e Entidades
Exemplo: em uma entidade "Cliente", atributos podem incluir nome, idade, e-mail, etc.

2. Entidades: Objetos do mundo real representados no banco de dados. Exemplo: "Cliente", "Produto", "Venda", etc.

3. Cardinalidade: Define o número de instâncias de uma entidade que podem estar associadas a instâncias de outra entidade. Exemplo: "um para um", "um para muitos", "muitos para muitos".

4. Criação de Tabelas
Utilizando um sistema de gerenciamento de banco de dados (SGBD) como MySQL, PostgreSQL, SQLServer dentre outros  criaremos tabelas para armazenar dados de acordo com as entidades identificadas e seus atributos.

5. Consultas para Análise de Dados
Utilizaremos consultas SQL para extrair informações úteis do banco de dados, como estatísticas, tendências e padrões.

# Exportação de Dados para Desenvolvimento de Machine Learning
Após a criação e análise dos dados, podemos exportá-los para o desenvolvimento de modelos de machine learning. Os passos  incluem

1. Extração de Dados: Exportar os dados do banco de dados para um formato adequado para análise, como CSV, JSON ou diretamente para estruturas de dados Python.

2. Pré-processamento de Dados: Limpar os dados, preencher valores ausentes, normalizar ou padronizar os dados, e realizar outras transformações necessárias para preparar os dados para modelagem.

3. Divisão de Dados: Separar os dados em conjuntos de treinamento, validação e teste.

4. Desenvolvimento do Modelo de Machine Learning: Utilizar bibliotecas como Scikit-learn, TensorFlow ou PyTorch para construir e treinar modelos de machine learning.

# Modelo de Deploy em Streamlit

Streamlit é uma biblioteca Python para a criação de aplicativos da web para análise de dados e machine learning de forma simples e rápida. Para criar um modelo de deploy em Streamlit, os passos podem incluir:

1. Desenvolvimento do Aplicativo: Escrever o código do aplicativo Streamlit, que inclui a definição da interface do usuário e a integração com o modelo de machine learning.

2. Implantação do Aplicativo: Utilizar plataformas de hospedagem como Azure, AWS, ou Google Cloud Platform para implantar o aplicativo .

3. Teste e Manutenção: Testar o aplicativo implantado para garantir seu funcionamento adequado e realizar manutenção conforme necessário.


# Instruções para instalação

```bash
conda create -n stenv python=3.8
conda activate stenvaa
pip install -r Requirements.txt
```
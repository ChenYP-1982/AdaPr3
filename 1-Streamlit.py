import pandas as pd
import pickle 
import streamlit as st

st.set_page_config(
    page_title="Pesquisa de satisfacao dos clientes",
    page_icon="🤖"
)

st.sidebar.header("Projeto end-to-end da disciplina de Banco de dados\n Inserir descricao do projeto")

st.write ("# :blue[Bem vindo ao  da Ada Consultas pesquisa de satisfacao ] 🩺")

st.markdown(
'''
O aplicativo trabalha com as seguintes features\n
1. Crm\n
2. Sexo\n
3. Idade\n
4. Especialidade\n
''')

Idade=st.number_input(label="idade", 
                    value=18,
                    min_value=18,
                    max_value=120)
Crm=st.selectbox(label="medico_id", 
                 options=['100045/SP', 
        '100038/RJ', '100085/SP', '100024/SP', '100092/SP',
       '100035/SP', '100079/SP', '100033/RJ', '100002/RJ', '100090/SP',
       '100060/RJ', '100038/SP', '100020/SP', '100032/SP', '100001/SP',
       '100074/SP', '100047/SP', '100017/SP', '100031/RJ', '100093/SP',
       '100049/RJ', '100070/SP', '100097/SP', '100010/RJ', '100015/SP',
       '100055/SP'])
Especialidade=st.selectbox(label="especialidade", 
                 options=['Psicologo', 'Oncologia', 
                        'Oftalmologia', 'Cardiologista',
                        'Ginecologista', 'Cirurgiao Plastico', 
                        'Endocrinologia','Pediatra', 'Urologista', 'Neurologia', 'Ortopedia'
                        ])
Sexo = st.radio(
    "Selecione o genero",
    ["Female", "Male","Outros"])
st.write("Voce selecionou:", Sexo)
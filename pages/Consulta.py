import streamlit as st
import pandas as pd


st.set_page_config(
    'Consulta de Cadastros',
    page_icon="padaria.png",
    layout='wide',
)


pessoas_cadastradas = pd.read_csv("clientes.csv")


st.title('Consulta ao Cadastro Padarias Iguaçu 🍞')
st.divider()


st.header("Pessoas Cadastradas:")
st.dataframe(
    pessoas_cadastradas,
    hide_index=True,
    column_config={
    'nome': st.column_config.TextColumn(
        "Nome_Cliente",
        help='Nome dos Clientes Cadastrados',
    ),
    
    'data_nascimento': st.column_config.TextColumn(
        'Data de Nascimento',
        help='A data de nascimento dos clientes'
    ),
    
    'tipo_pessoa': st.column_config.TextColumn(
        'Tipo do Cliente',
        help='(Pessoa física/Pessoa jurídica)'
    )
    
    },
    width=1300             
)



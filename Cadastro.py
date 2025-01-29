import streamlit as st
import datetime as dt


st.set_page_config(page_title='Sistema Padaria Iguaçu',
                   page_icon='padaria.png',
                   layout='wide')

                   
lateral = st.sidebar


def gravar_dados(nome, data_nascimento, tipo_pessoa):
    if nome and data_nascimento and tipo_pessoa:
        if data_nascimento <= dt.date.today():
            st.session_state['sucesso'] = True
            with open("clientes.csv", "a", encoding='utf-8') as file:
                file.write(f'\n{nome},{data_nascimento},{tipo_pessoa}')
        else:
            st.session_state['sucesso'] = False 
    else:
        st.session_state['sucesso'] = False 


if 'desabilitado' not in st.session_state:
    st.session_state['desabilitado'] = False


if 'sucesso' not in st.session_state:
    st.session_state['sucesso'] = False
    
    
if 'verificador' not in st.session_state:
    st.session_state['verificador'] = 0


st.title('Cadastro de Clientes Padaria Iguaçu 🍞')
st.divider()


nome = st.text_input("Digite seu nome:",
                     key='nome_cliente',
                     disabled=st.session_state['desabilitado'])


data_nascimento = st.date_input('Entre com sua data de nascimento:',
                                format='DD/MM/YYYY',
                                key='data_nascimento_cliente',
                                value=None,
                                min_value=dt.date(1900, 1, 1),
                                max_value=dt.date.today(),
                                disabled=st.session_state['desabilitado'])



tipo_pessoa = st.selectbox('Selecione o seu tipo de pessoa:',
                           ['Pessoa física', 'Pessoa jurídica'],
                           index=None,
                           disabled=st.session_state['desabilitado'])


col1, col2, col3, col4, col5, col6, col7  = st.columns(7)


botao_cadastrar = col1.button('Clique para Cadastrar',
                            on_click=gravar_dados,
                            args=[nome, data_nascimento, tipo_pessoa],
                            use_container_width=True)


if botao_cadastrar:
    if st.session_state['verificador'] > 0 and st.session_state['desabilitado']:
        st.warning('Seus dados já foram cadastrados. Para alterar clique no botão "Alterar Cadastro"')
        st.session_state['verificador'] += 1
        botao_cadastrar = False
        
    else:
        if st.session_state['sucesso']:
            st.session_state['desabilitado'] = True
            botao_cadastrar=False
            st.session_state['verificador'] += 1
            st.rerun()
                       
        elif botao_cadastrar:
            st.error('Preencha todos os campos corretamente',
                        icon='❌')
            botao_cadastrar=False

            
if st.session_state['desabilitado']:
    
    alterar_cadastro = col2.button("Alterar Cadastro",
                               use_container_width=True)
    
    if alterar_cadastro:
        st.session_state['desabilitado'] = False
        alterar_cadastro = False
        st.session_state['verificador'] = 0
        st.rerun()
    
    if st.session_state['verificador'] == 1:
        st.success('Cadastro realizado com SUCESSO',
                        icon='✅')
    

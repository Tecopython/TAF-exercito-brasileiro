import pandas as pd
from pathlib import Path
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import funcoes as f

#IMPORTANDO A PLANILHA PARA UM DATAFRAME
diretorio_atual = Path.cwd()
arquivo = diretorio_atual/'PLANILHA TAF.xlsx'
arquivo_excel = pd.ExcelFile(arquivo)#variável recebe todo o arquivo exel com suas abas
dfs = [pd.read_excel(arquivo_excel,sheet_name=sheet).assign(TAF=sheet) for sheet in arquivo_excel.sheet_names] #cria uma lista com as abas da planilha
tabela_tafs = pd.concat(dfs,ignore_index=True)#concatena as abas da planilha em uma só


######### INICIANDO A CRIAÇÃO DA PÁGINA
# CONFIGURANDO A PÁGINA
st.set_page_config(
     layout='wide',
     page_title='TAF - 10º BIL Mth',
 )
#TÍTULO
st.markdown("<h1 style='text-align: center;'>TAF - 10º BIL Mth</h1>", unsafe_allow_html=True)

######CRIANDO A MOLDURA DOS BOTÕES DO TAF
with st.container(border=True):
    col1,col2,col3 = st.columns(3) #cria 3 colunas
    taf_1 = col1.checkbox('1º TAF',value=True)
    taf_2 = col2.checkbox('2º TAF')
    taf_3 = col3.checkbox('3º TAF')

#FILTRANDO A TABELA PELOS TAF ESCOLHIDOS
tabela_do_taf = f.pega_taf(tabela_tafs,taf_1,taf_2,taf_3)#pegando os taf selecionados

#CRIANDO AS COLUNAS CENTRAIS
col_central = st.columns([1, 4, 1])[1] #criando as colunas

col4, mid_col, col7 = st.columns([0.15,0.7,0.15], vertical_alignment='center')
col5,col6 = mid_col.columns(2, vertical_alignment='center')

#CONFIGURANDO OS MENUS DA ESQUERDA
with col4:
    #CRIANDO MENUS COM SELEÇÃO DE IDADE, EXERCÍCIOS E MENÇÕES
    st.subheader('ITENS / CONSULTA')
    idade = st.checkbox('IDADE',value=True)
    if idade:
        escolha_idade = st.selectbox('escolha',('TODAS','18-21','22-25','26-29','30-33','34-37','38-41','42-45','46-49','>=50'),label_visibility='hidden', placeholder='Escolha a faixa etária', index=None)
    else:
        escolha_idade = None
    corrida = st.checkbox('CORRIDA')
    flexao = st.checkbox('FLEXÃO')
    abdominal = st.checkbox('ABDOMINAL')
    barra = st.checkbox('BARRA')
    mencao = st.checkbox('MENÇÃO')
    #CRIANDO MENUS COM AS CHAMADAS
    st.subheader('CHAMADAS')
    primeira_chamada = st.checkbox('1ª Chamada',value=True)
    segunda_chamada = st.checkbox('2ª Chamada',value=True)
    nr = st.checkbox('Não Realizado')

# CONFIGURANDO O MENU DA DIREITA
with col7:
    #CRIANDO MENU PARA AS SU
    lista_su = ['Geral','1ª Cia Fuz L Mth', '2ª Cia Fuz L Mth','Cia C Ap', 'CFGS','B Mus']
    st.subheader('SUBUNIDADES')
    escolha_su = st.radio('**SUBUNIDADES**', options=lista_su, index=1, label_visibility='hidden')
    #CRIANDO MENU PARA ESCOLHA DO POSTO / GRADUAÇÃO
    st.subheader('POSTOS E GRADUAÇÕES')
    oficiais = st.checkbox('Oficiais',value=True)
    st_sgt = st.checkbox('ST e Sgt')
    cb_sd_ep = st.checkbox('Cb/Sd EP')
    sd_ev = st.checkbox('Sd EV')

#FILTRAR AS TABELA COM AS OPÇÕES ESCOLHIDAS NOS MENUS
tabela_filtrada =(f.filtra_su(
    f.filtra_pg(
        f.filtra_chamadas(
            f.pega_taf(tabela_tafs,taf_1,taf_2,taf_3)
        ,primeira_chamada,segunda_chamada,nr)
    ,oficiais,st_sgt,cb_sd_ep,sd_ev)
,escolha_su)
)

#FILTRANDO POR IDADE O QUE SOBROU DA TABELA
tabela_filtrada_idade = f.filtra_idade(tabela_filtrada,escolha_idade)
tabela_filtrada_idade


if idade:
    if corrida:
        if flexao:
            if abdominal:
                if barra:
                    if mencao:#Todos os itens
                        with mid_col:
                            st.subheader(f'Para idade entre {escolha_idade}')
                            st.dataframe(tabela_filtrada.drop(columns=['OBS', 'COMPANHIA', 'CHAMADA', 'GRÁFICOS','TAF','BI Publicado']))
                    else:#('**SIM** - idade - corrida - flexão - abdominal - barra')('**NÃO** - menção')
                        col5.write('**SIM** - idade - corrida - flexão - abdominal - barra')
                        col6.write('**NÃO** - menção')
                        #colocar gráfico de pontos
                else:
                    if mencao:
                        col5.write('**SIM** - idade - corrida - flexão - abdominal - menção')
                        col6.write('**NÃO** - barra')
                    else:
                        col5.write('**SIM** - idade - corrida - flexão - abdominal')
                        col6.write('**NÃO** - barra - menção')
            else:
                if barra:
                    if mencao:
                        col5.write('**SIM** - idade - corrida - flexão - barra - menção')
                        col6.write('**NÃO** - abdominal')
                    else:
                        col5.write('**SIM** - idade - corrida - flexão - barra')
                        col6.write('**NÃO** - abdominal - menção')
                else:
                    if mencao:
                        col5.write('**SIM** - idade - corrida - flexão - menção')
                        col6.write('**NÃO** - abdominal - barra')
                    else:
                        col5.write('**SIM** - idade - corrida - flexão')
                        col6.write('**NÃO** - abdominal - barra - menção')
        else:
            if abdominal:
                if barra:
                    if mencao:
                        col5.write('**SIM** - idade - corrida - abdominal - barra - menção')
                        col6.write('**NÃO** - flexão')
                    else:
                        col5.write('**SIM** - idade - corrida - abdominal - barra')
                        col6.write('**NÃO** - flexão - menção')
                else:
                    if mencao:
                        col5.write('**SIM** - idade - corrida - abdominal- menção')
                        col6.write('**NÃO** - flexão - barra')
                    else:
                        col5.write('**SIM** - idade - corrida - abdominal')
                        col6.write('**NÃO** - flexão - barra - menção')
            else:
                if barra:
                    if mencao:
                        col5.write('**SIM** - idade - corrida - barra - menção')
                        col6.write('**NÃO** - flexão - abdominal')
                    else:
                        col5.write('**SIM** - idade - corrida - barra')
                        col6.write('**NÃO** - flexão - abdominal - menção')
                else:
                    if mencao:
                        col5.write('**SIM** - idade - corrida - menção')
                        col6.write('**NÃO** - flexão - abdominal - barra')
                    else:
                        col5.write('**SIM** - idade - corrida')
                        col6.write('**NÃO** - flexão - abdominal - barra - menção')
    else:# corrida não
        if flexao:
            if abdominal:
                if barra:
                    if mencao:
                        col5.write('**SIM** - idade - flexão - abdominal - barra - menção')
                        col6.write('**NÃO** - corrida')
                    else:
                        col5.write('**SIM** - idade - flexão - abdominal - barra')
                        col6.write('**NÃO** - corrida - menção')
                else:
                    if mencao:
                        col5.write('**SIM** - idade - flexão - abdominal- menção')
                        col6.write('**NÃO** - corrida - barra')
                    else:
                        col5.write('**SIM** - idade - flexão - abdominal')
                        col6.write('**NÃO** - corrida - barra - menção')
            else: #corrida abdominal não
                if barra:
                    if mencao:
                        col5.write('**SIM** - idade - flexão - barra - menção')
                        col6.write('**NÃO** - corrida - abdominal')
                    else:
                        col5.write('**SIM** - idade - flexão - barra')
                        col6.write('**NÃO** - corrida - abdominal - menção')
                else:#barra não
                    if mencao:
                        col5.write('**SIM** - idade - flexão - menção')
                        col6.write('**NÃO** - corrida - abdominal - barra')
                    else:
                        col5.write('**SIM** - idade - flexão')
                        col6.write('**NÃO** - corrida - abdominal - barra - menção')
        else: #corrida - flexão - não
            if abdominal:
                if barra:
                    if mencao:
                        col5.write('**SIM** - idade - abdominal - barra - menção')
                        col6.write('**NÃO** - corrida - flexão')
                    else:
                        col5.write('**SIM** - idade - abdominal - barra')
                        col6.write('**NÃO** - corrida - flexão - menção')
                else:
                    if mencao:
                        col5.write('**SIM** - idade - abdominal - menção')
                        col6.write('**NÃO** - corrida - flexão - barra')
                    else:
                        col5.write('**SIM** - idade - abdominal')
                        col6.write('**NÃO** - corrida - flexão - barra - menção')
            else: #corrida - flexão - abdominal
                if barra:
                    if mencao:
                        col5.write('**SIM** - idade - barra - menção')
                        col6.write('**NÃO** - corrida - flexão - abdominal')
                    else:
                        col5.write('**SIM** - idade - barra')
                        col6.write('**NÃO** - corrida - flexão - abdominal - menção')
                else:#barra não
                    if mencao:
                        col5.write('**SIM** - idade - menção')
                        col6.write('**NÃO** - corrida- flexão - abdominal - barra')
                    else:
                        col5.write('**SIM** - idade')
                        col6.write('**NÃO** - corrida - flexão - abdominal - barra - menção')
else: #idade não
    if corrida:
        if flexao:
            if abdominal:
                if barra:
                    if mencao:
                        with mid_col:
                            st.dataframe(tabela_filtrada.drop(columns=['IDADE','OBS', 'COMPANHIA', 'CHAMADA', 'GRÁFICOS','TAF','BI Publicado']))
                    else: #idade - menção  não
                        col5.write('**SIM**-  corrida - flexão - abdominal - barra')
                        col6.write('**NÃO** - idade - menção')
                        #colocar gráfico de pontos
                else:#idade - barra -não
                    if mencao:
                        col5.write('**SIM** - corrida - flexão - abdominal - menção')
                        col6.write('**NÃO** - idade - barra')
                    else:
                        col5.write('**SIM** - corrida - flexão - abdominal')
                        col6.write('**NÃO** - idade - barra - menção')
            else:#idade - abdominal não
                if barra:
                    if mencao:
                        col5.write('**SIM** - corrida - flexão - barra - menção')
                        col6.write('**NÃO** - idade - abdominal')
                    else:
                        col5.write('**SIM** - corrida - flexão - barra')
                        col6.write('**NÃO** - idade - abdominal - menção')
                else:
                    if mencao:
                        col5.write('**SIM** - corrida - flexão - menção')
                        col6.write('**NÃO** - idade - abdominal - barra')
                    else:
                        col5.write('**SIM** - corrida - flexão')
                        col6.write('**NÃO** - idade - abdominal - barra - menção')
        else:
            if abdominal:
                if barra:
                    if mencao:
                        col5.write('**SIM** - corrida - abdominal - barra - menção')
                        col6.write('**NÃO** - idade - flexão')
                    else:
                        col5.write('**SIM** - corrida - abdominal - barra')
                        col6.write('**NÃO** - idade - flexão - menção')
                else:
                    if mencao:
                        col5.write('**SIM** - corrida - abdominal- menção')
                        col6.write('**NÃO** - idade - flexão - barra')
                    else:
                        col5.write('**SIM** - corrida - abdominal')
                        col6.write('**NÃO** - idade - flexão - barra - menção')
            else:
                if barra:
                    if mencao:
                        col5.write('**SIM** - corrida - barra - menção')
                        col6.write('**NÃO** - idade - flexão - abdominal')
                    else:
                        col5.write('**SIM** - corrida - barra')
                        col6.write('**NÃO** - idade - flexão - abdominal - menção')
                else:
                    if mencao:
                        col5.write('**SIM** - corrida - menção')
                        col6.write('**NÃO** - idade - flexão - abdominal - barra')
                    else:
                        col5.write('**SIM** - corrida')
                        col6.write('**NÃO** - idade - flexão - abdominal - barra - menção')
    else:# corrida não
        if flexao:
            if abdominal:
                if barra:
                    if mencao:
                        col5.write('**SIM** - flexão - abdominal - barra - menção')
                        col6.write('**NÃO** - idade - corrida')
                    else:
                        col5.write('**SIM** - flexão - abdominal - barra')
                        col6.write('**NÃO** - idade - corrida - menção')
                else:
                    if mencao:
                        col5.write('**SIM** - flexão - abdominal- menção')
                        col6.write('**NÃO** - idade - corrida - barra')
                    else:
                        col5.write('**SIM** - flexão - abdominal')
                        col6.write('**NÃO** - idade - corrida - barra - menção')
            else: #corrida abdominal não
                if barra:
                    if mencao:
                        col5.write('**SIM** - flexão - barra - menção')
                        col6.write('**NÃO** -idade -  corrida - abdominal')
                    else:
                        col5.write('**SIM** - flexão - barra')
                        col6.write('**NÃO** -idade -  corrida - abdominal - menção')
                else:#barra não
                    if mencao:
                        col5.write('**SIM** - flexão - menção')
                        col6.write('**NÃO** -idade -  corrida - abdominal - barra')
                    else:
                        col5.write('**SIM** - flexão')
                        col6.write('**NÃO** -idade -  corrida - abdominal - barra - menção')
        else: #corrida - flexão - não
            if abdominal:
                if barra:
                    if mencao:
                        col5.write('**SIM** - abdominal - barra - menção')
                        col6.write('**NÃO** - idade - corrida - flexão')
                    else:
                        col5.write('**SIM** - abdominal - barra')
                        col6.write('**NÃO** - idade - corrida - flexão - menção')
                else:
                    if mencao:
                        col5.write('**SIM** - abdominal - menção')
                        col6.write('**NÃO** - idade - corrida - flexão - barra')
                    else:
                        col5.write('**SIM** - abdominal')
                        col6.write('**NÃO** - idade - corrida - flexão - barra - menção')
            else: #corrida - flexão - abdominal
                if barra:
                    if mencao:
                        col5.write('**SIM** - barra - menção')
                        col6.write('**NÃO** - idade - corrida - flexão - abdominal')
                    else:
                        col5.write('**SIM** - barra')
                        col6.write('**NÃO** - idade - corrida - flexão - abdominal - menção')
                else:#barra não
                    if mencao:#('**SIM** - menção')('**NÃO** - idade - corrida- flexão - abdominal - barra')
                        with col5:
                            st.pyplot(f.grafico_pizza(tabela_filtrada))
                        with col6:
                            st.dataframe(tabela_filtrada.drop(columns=['OBS', 'COMPANHIA', 'CHAMADA','TAF','BI Publicado','CORRIDA','BARRA','ABDOMINAL','FLEXÃO']))
                    else:#(tudo desmarcado)
                        with mid_col:
                            st.dataframe(tabela_filtrada_idade)


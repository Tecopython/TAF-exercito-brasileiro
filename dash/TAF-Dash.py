# -*- coding: utf-8 -*-

import pandas as pd
from pathlib import Path
import streamlit as st
import funcoes as f
import plotly.express as px
from tabela_indice import *

#DEFININDO CAMINHO PARA O ARQUIVO, DEVERÁ ESTÁR NO MESMO DIRETÓRIO DO SCRIPT
diretorio_atual = Path.cwd()
arquivo = diretorio_atual/'PLANILHA TAF.xlsx'

######### INICIANDO A CRIAÇÃO DA PÁGINA
# CONFIGURANDO A PÁGINA
st.set_page_config(
     layout='wide',
     page_title='Dash TAF - 10º BIL Mth',
 )
@st.cache_data #Jogando a tabela para a memória, não precisa carregar toda vez
def pega_excel(arquivo):
    arquivo_excel = pd.ExcelFile(arquivo)#variável recebe todo o arquivo exel com suas abas
    dfs = [pd.read_excel(arquivo_excel,sheet_name=sheet).assign(TAF=sheet) for sheet in arquivo_excel.sheet_names] #cria uma lista com as abas da planilha
    tabela_tafs = pd.concat(dfs,ignore_index=True)#concatena as abas da planilha em uma só
    return tabela_tafs

#carregando a tabela num DataFrame
tabela_tafs = pega_excel(arquivo)
#limpando as colunas 'rolhas'
tabela_tafs.drop(columns=['OBS','BI Publicado'], inplace=True)

#TÍTULO
st.markdown("<h1 style='text-align: center;'>TAF - 10º BIL Mth</h1>", unsafe_allow_html=True)

######CRIANDO A MOLDURA DOS BOTÕES DO TAF
with st.container(border=True):
    col1,col2,col3 = st.columns(3) #cria 3 colunas
    taf_1 = col1.checkbox('1º TAF',value=True)
    taf_2 = col2.checkbox('2º TAF')
    taf_3 = col3.checkbox('3º TAF')

#Criando as colunas (três colunas com a do meio maior)
col4, mid_col, col7 = st.columns([0.15,0.7,0.15], vertical_alignment='center')
#Dividindo a coluna do meio em duas
col5,col6 = mid_col.columns([1,3], vertical_alignment='center')

#CONFIGURANDO OS MENUS DA ESQUERDA
with col4:
    #CRIANDO MENUS COM SELEÇÃO DE IDADE, EXERCÍCIOS E MENÇÕES
    st.subheader('ITENS / CONSULTA')
    idade = st.checkbox('IDADE')
    if idade:
        escolha_idade = st.selectbox('escolha',('TODAS','18-21','22-25','26-29','30-33','34-37','38-41','42-45','46-49','>=50'),label_visibility='hidden', placeholder='Escolha a faixa etária', index=None)
    else:
        escolha_idade = None
    segmento = st.checkbox('SEGMENTO')
    mas, fem = True, True #colocado só para evitar o erro na linha 84 caso a checkbox do segmento não seja selecionada.
    if segmento:
        mas = st.checkbox('MASCULINO', value=True)
        fem = st.checkbox('FEMININO', value=True)
    corrida = st.checkbox('CORRIDA')
    flexao = st.checkbox('FLEXÃO')
    abdominal = st.checkbox('ABDOMINAL')
    barra = st.checkbox('BARRA')
    mencao = st.checkbox('MENÇÃO', value=True)
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
    escolha_su = st.radio('**SUBUNIDADES**', options=lista_su, index=0, label_visibility='hidden')
    #CRIANDO MENU PARA ESCOLHA DO POSTO / GRADUAÇÃO
    st.subheader('POSTOS E GRADUAÇÕES')
    oficiais = st.checkbox('Oficiais',value=True)
    st_sgt = st.checkbox('ST e Sgt')
    cb_sd_ep = st.checkbox('Cb/Sd EP')
    sd_ev = st.checkbox('Sd EV')

#FILTRAR AS TABELA COM AS OPÇÕES ESCOLHIDAS NOS MENUS
tabela_filtrada = f.filtra_su(
                              f.filtra_pg(
                                          f.filtra_chamadas(
                                                            f.filtra_segmento(
                                                                              f.pega_taf(tabela_tafs,taf_1,taf_2,taf_3)
                                                            ,segmento, mas, fem)
                                          ,primeira_chamada,segunda_chamada,nr)
                              ,oficiais,st_sgt,cb_sd_ep,sd_ev)
                  ,escolha_su)


#FILTRANDO POR IDADE O QUE SOBROU DA TABELA
tabela_filtrada_idade = f.filtra_idade(tabela_filtrada,escolha_idade)
#CRIA UMA TABELA COM AS MENÇÕES POR ATIVIDADE
tabela_mencao_atividades = f.criar_coluna_mencao_atividade(tabela_filtrada_idade)
#MOSTRAR A TABELA FILTRADA AO FINAL DA PÁGINA.
st.markdown("<h2 style='text-align: center;'>Tabela com os filtros aplicados</h1>", unsafe_allow_html=True)
#MONSTRAR A TABELA FILTRADA NO FINAL DA PÁGINA.
tabela_filtrada_idade


if idade:
    if corrida:
        if flexao:
            if abdominal:
                if barra:
                    if mencao:#Todos os itens
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                        #with mid_col:
                            # st.subheader(f'Para idade entre {escolha_idade}')
                            # st.dataframe(tabela_filtrada_idade.drop(columns=['COMPANHIA', 'CHAMADA','TAF',]))
                    else:#IDADE - CORRIDA - FLEXÃO - ABDOMINAL - BARRA
                        col5.write('Gráfico comparativo das menções por cada atividade')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra))
                else:
                    if mencao:# IDADE - CORRIDA - FLEXÃO - ABDOMINAL - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else:#IDADE - CORRIDA - FLEXÃO - ABDOMINAL
                        col5.write('Gráfico comparativo das menções por cada atividade')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra))
            else:
                if barra:
                    if mencao:#IDADE - CORRIDA - FLEXÃO - BARRA - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else:#IDADE - CORRIDA - FLEXÃO - BARRA
                        col5.write('Gráfico comparativo das menções por cada atividade')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra))
                else:
                    if mencao:# IDADE - CORRIDA - FLEXÃO - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else:#IDADE - CORRIDA - FLEXÃO
                        col5.write('Gráfico comparativo das menções por cada atividade')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra))
        else:
            if abdominal:
                if barra:
                    if mencao:# IDADE - CORRIDA - ABDOMINAL - BARRA - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else:#IDADE - CORRIDA - ABDOMINAL - BARRA
                        col5.write('Gráfico comparativo das menções por cada atividade')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra))
                else:
                    if mencao:# IDADE - CORRIDA - ABDOMINAL - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else:#IDADE - CORRIDA - ABDOMINAL
                        col5.write('Gráfico comparativo das menções por cada atividade')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra))
            else:
                if barra:
                    if mencao:#IDADE - CORRIDA - BARRA - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else:#IDADE - CORRIDA - BARRA
                        col5.write('Gráfico comparativo das menções por cada atividade')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra))
                else:
                    if mencao:# IDADE - CORRIDA - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else: #IDADE E CORRIDA
                        col5.write(f'Este gráfico de disperção mostra o desempenho na CORRIDA por SEGMENTO E IDADE -> {escolha_idade} anos')
                        with col6:
                            f.idade_seg_atv(tabela_filtrada_idade, 'CORRIDA')
    else:# corrida não
        if flexao:
            if abdominal:
                if barra:
                    if mencao:# IDADE - FLEXÃO - ABDOMINAL - BARRA - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else:#IDADE - FLEXÃO - ABDOMINAL - BARRA
                        col5.write('Gráfico comparativo das menções por cada atividade')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra))
                else:
                    if mencao:# IDADE - FLEXÃO - ABDOMINAL - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else:# IDADE - FLEXÃO - ABDOMINAL
                        col5.write('Gráfico comparativo das menções por cada atividade')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra))
            else: #corrida abdominal não
                if barra:
                    if mencao:# IDADE - FLEXÃO - BARRA - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else:#IDADE - FLEXÃO - BARRA
                        col5.write('Gráfico comparativo das menções por cada atividade')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra))
                else:#barra não
                    if mencao:# IDADE - FLEXÃO - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else:# IDADE E FLEXÃO
                        col5.write(f'Este gráfico de disperção mostra o desempenho na FLEXÃO DE BRAÇO por SEGMENTO E IDADE -> {escolha_idade} anos')
                        with col6:
                            f.idade_seg_atv(tabela_filtrada_idade, 'FLEXÃO')
        else: #corrida - flexão - não
            if abdominal:
                if barra:
                    if mencao:# IDADE - ABDOMINAL - BARRA - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else:#IDADE - ABDOMINAL - BARRA
                        col5.write('Gráfico comparativo das menções por cada atividade')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra))
                else:
                    if mencao:# IDADE - ABDOMINAL - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else:# IDADE E ABDOMINAL
                        col5.write(f'Este gráfico de disperção mostra o desempenho no ABDOMINAL por SEGMENTO E IDADE -> {escolha_idade} anos')
                        with col6:
                            f.idade_seg_atv(tabela_filtrada_idade, 'ABDOMINAL')
            else: #corrida - flexão - abdominal
                if barra:
                    if mencao:# IDADE - BARRA - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else: #IDADE E BARRA
                        col5.write(f'Este gráfico de disperção mostra o desempenho na BARRA por SEGMENTO E IDADE -> {escolha_idade} anos')
                        with col6:
                            f.idade_seg_atv(tabela_filtrada_idade, 'BARRA')
                else:#barra não
                    if mencao:#MENÇÃO E IDADE
                        with col5:
                            st.write('O gráfico apresenta a distribuição da menção final do(s) TAF(s) selecionado(s), podendo ser alterado o SEGMENTO e a IDADE')
                        with col6:
                            st.pyplot(f.grafico_pizza(tabela_filtrada_idade, "MENÇÃO"))
                        with col6:
                            fig_mencoes = f.graf_linhas_mencoes_por_taf(tabela_filtrada_idade)
                            st.plotly_chart(fig_mencoes, use_container_width=True)
                    else:#SOMENTE IDADE
                        col5.write('**SIM** - idade')
                        col6.write('**NÃO** - corrida - flexão - abdominal - barra - menção')
else: #idade não
    if corrida:
        if flexao:
            if abdominal:
                if barra:
                    if mencao:
                        with mid_col:
                            st.dataframe(tabela_filtrada_idade)
                    else: #CORRIDA FLEXÃO ABDOMINAL BARRA
                        col5.write('Gráfico comparativo das menções por cada atividade')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra))
                       
                else:#idade - barra -não
                    if mencao:# CORRIDA - FLEXÃO - ABDOMINAL - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else:# CORRIDA - FLEXÃO - ABDOMINAL
                        col5.write('Gráfico comparativo das menções por cada atividade')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra))
            else:#idade - abdominal não
                if barra:
                    if mencao:# CORRIDA - FLEXÃO - BARRA - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else:# CORRIDA - FLEXÃO - BARRA
                        col5.write('Gráfico comparativo das menções por cada atividade')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra))
                else:
                    if mencao:# CORRIDA - FLEXÃO - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else:#CORRIDA - FLEXÃO
                        col5.write('Gráfico comparativo das menções por cada atividade')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra))
        else:
            if abdominal:
                if barra:
                    if mencao:# CORRIDA - ABDOMINAL - BARRA - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else:#CORRIDA - ABDOMINAL - BARRA
                        col5.write('Gráfico comparativo das menções por cada atividade')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra))
                else:
                    if mencao:# CORRIDA - ABDOMINAL - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else:#CORRIDA - ABDOMINAL
                        col5.write('Gráfico comparativo das menções por cada atividade')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra))
            else:
                if barra:
                    if mencao:# CORRIDA - BARRA - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else:#CORRIDA - BARRA
                        col5.write('Gráfico comparativo das menções por cada atividade')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra))
                else:
                    if mencao:#CORRIDA - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else:#SOMENTE CORRIDA
                        tabela_filtrada_idade = tabela_filtrada_idade[~((tabela_filtrada_idade["CORRIDA"] == 'A') | (tabela_filtrada_idade["CORRIDA"].isna()) | (tabela_filtrada_idade["CORRIDA"] == 'X'))] # trata a tabela para tirar "A", nulo e 'X'
                        tabela_filtrada_idade["Menção na corrida"] = tabela_filtrada_idade.apply(lambda row: f.determinar_mencao(row['IDADE'],dicio_atividades,'CORRIDA', row['LEM'], row['SEGMENTO'], row['CORRIDA']), axis=1)
                        with col5:
                            st.dataframe(tabela_filtrada_idade["Menção na corrida"].value_counts())
                        with col6:
                            st.pyplot(f.grafico_pizza(tabela_filtrada_idade, "Menção na corrida"))
    else:# corrida não
        if flexao:
            if abdominal:
                if barra:
                    if mencao:# FLEXÃO - ABDOMINAL - BARRA - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else:#FLEXÃO - ABDOMINAL - BARRA
                        col5.write('Gráfico comparativo das menções por cada atividade')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra))
                else:
                    if mencao:# FLEXÃO - ABDOMINAL - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else:#FLEXÃO - ABDOMINAL
                        col5.write('Gráfico comparativo das menções por cada atividade')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra))
            else: #corrida abdominal não
                if barra:
                    if mencao:# FLEXÃO - BARRA - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else:# FLEXÃO - BARRA
                        col5.write('Gráfico comparativo das menções por cada atividade')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra))
                else:#barra não
                    if mencao:# FLEXÃO - MENÇÃO
                        col5.write('**SIM** - flexão - menção')
                        col6.write('**NÃO** -idade -  corrida - abdominal - barra')
                    else: #SOMENTE FLEXÃO
                        tabela_filtrada_idade = tabela_filtrada_idade[~((tabela_filtrada_idade["FLEXÃO"] == 'A') | (tabela_filtrada_idade["FLEXÃO"].isna()) | (tabela_filtrada_idade["FLEXÃO"] == 'X'))] # trata a tabela para tirar "A", nulo e 'X'
                        tabela_filtrada_idade["Menção na flexão"] = tabela_filtrada_idade.apply(lambda row: f.determinar_mencao(row['IDADE'],dicio_atividades,'FLEXAO', row['LEM'], row['SEGMENTO'], row['FLEXÃO']), axis=1)
                        with col5:
                            st.dataframe(tabela_filtrada_idade["Menção na flexão"].value_counts())
                        with col6:
                            st.pyplot(f.grafico_pizza(tabela_filtrada_idade, "Menção na flexão"))
        else: #corrida - flexão - não
            if abdominal:
                if barra:
                    if mencao:# ABDOMINAL - BARRA - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else:#ABDOMINAL - BARRA
                        col5.write('Gráfico comparativo das menções por cada atividade')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra))
                else:
                    if mencao:# ABDOMINAL - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else:# SOMENTE ABDOMINAL
                        tabela_filtrada_idade = tabela_filtrada_idade[~((tabela_filtrada_idade["ABDOMINAL"] == 'A') | (tabela_filtrada_idade["ABDOMINAL"].isna()) | (tabela_filtrada_idade["ABDOMINAL"] == 'X'))] # trata a tabela para tirar "A", nulo e 'X'
                        tabela_filtrada_idade["Menção no abdominal"] = tabela_filtrada_idade.apply(lambda row: f.determinar_mencao(row['IDADE'],dicio_atividades,'ABDOMINAL', row['LEM'], row['SEGMENTO'], row['ABDOMINAL']), axis=1)
                        with col5:
                            st.dataframe(tabela_filtrada_idade["Menção no abdominal"].value_counts())
                        with col6:
                            st.pyplot(f.grafico_pizza(tabela_filtrada_idade, "Menção no abdominal"))
            else: #corrida - flexão - abdominal
                if barra:
                    if mencao:# BARRA - MENÇÃO
                        col5.write('Gráfico comparativo das menções por cada atividade com a menção geral')
                        with col6:
                            st.plotly_chart(f.grafico_linha(tabela=tabela_mencao_atividades, corrida=corrida, flexao=flexao, abdominal=abdominal, barra=barra, mencao=mencao))
                    else:# SOMENTE BARRA
                        tabela_filtrada_idade = tabela_filtrada_idade[~((tabela_filtrada_idade["BARRA"] == 'A') | (tabela_filtrada_idade["BARRA"].isna()) | (tabela_filtrada_idade["BARRA"] == 'X'))] # trata a tabela para tirar "A", nulo e 'X'
                        tabela_filtrada_idade["Menção na barra"] = tabela_filtrada_idade.apply(lambda row: f.determinar_mencao(row['IDADE'],dicio_atividades,'BARRA', row['LEM'], row['SEGMENTO'], row['BARRA']), axis=1)
                        with col5:
                            st.dataframe(tabela_filtrada_idade["Menção na barra"].value_counts())
                        with col6:
                            st.pyplot(f.grafico_pizza(tabela_filtrada_idade, "Menção na barra"))
                else:#barra não
                    if mencao:#SOMENTE MENÇÃO
                        with col5:
                            st.write('O gráfico apresenta a distribuição da menção final do(s) TAF(s) selecionado(s), podendo ser alterado o SEGMENTO e a IDADE')
                        with col6:
                            st.pyplot(f.grafico_pizza(tabela_filtrada_idade, "MENÇÃO"))
                        with col6:
                            fig_mencoes = f.graf_linhas_mencoes_por_taf(tabela_filtrada_idade)
                            st.plotly_chart(fig_mencoes, use_container_width=True)
                    else:#(tudo desmarcado)
                        with mid_col:
                            st.write('NENHUMA ATIVIDADE OU MENÇÃO SELECIONADA')


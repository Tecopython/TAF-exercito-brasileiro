import pandas as pd
from pathlib import Path
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(
     layout='wide',
     page_title='TAF - 10º BIL Mth',
 )
diretorio_atual = Path.cwd()
arquivo = diretorio_atual/'PLANILHA TAF.xlsx'
arquivo_excel = pd.ExcelFile(arquivo)#variável recebe todo o arquivo exel com suas abas
dfs = [pd.read_excel(arquivo_excel,sheet_name=sheet).assign(TAF=sheet) for sheet in arquivo_excel.sheet_names] #cria uma lista com as abas da planilha
tabela_tafs = pd.concat(dfs,ignore_index=True)#concatena as abas da planilha em uma só

# tabela = tabela_tafs[tabela_tafs['TAF'].isin(['1º TAF'])]
# tabela.reset_index(inplace=True, drop=True)
#########################################################################################
def pega_taf(tabela,taf_1=True, taf_2=False, taf_3=False):#filtra os TAF de acordo com os botões de seleção
    try:
        if taf_1 and not taf_2 and not taf_3:
            tabela = tabela[tabela['TAF'].isin(['1º TAF'])]
            tabela.reset_index(inplace=True, drop=True)
            return tabela
        elif taf_1 and taf_2 and not taf_3:
            tabela = tabela[tabela['TAF'].isin(['1º TAF', '2º TAF'])]
            tabela.reset_index(inplace=True, drop=True)
            return tabela
        elif taf_1 and not taf_2 and taf_3:
            tabela = tabela[tabela['TAF'].isin(['1º TAF','3º TAF'])]
            tabela.reset_index(inplace=True, drop=True)
            return tabela
        elif not taf_1 and taf_2 and not taf_3:
            tabela = tabela[tabela['TAF'].isin(['2º TAF'])]
            tabela.reset_index(inplace=True, drop=True)
            return tabela
        elif not taf_1 and taf_2 and taf_3:
            tabela = tabela[tabela['TAF'].isin(['2º TAF','3º TAF'])]
            tabela.reset_index(inplace=True, drop=True)
            return tabela
        elif taf_1 and taf_2 and taf_3:
            return tabela
        else:
            tabela = tabela[tabela['TAF'].isin(['3º TAF'])]
            tabela.reset_index(inplace=True, drop=True)
            return tabela
    except:
        return pd.DataFrame()


##############################################################################
def filtra_chamadas(tabela,primeira_chamada,segunda_chamada,nr=False):
    try:
        if primeira_chamada and not segunda_chamada and not nr:
            tabela = tabela[tabela['CHAMADA'].isin(['1ª Chamada'])]
            tabela.reset_index(inplace=True,drop=True)
            return tabela
        elif primeira_chamada and segunda_chamada and not nr:
            tabela = tabela[tabela['CHAMADA'].isin(['1ª Chamada','2ª Chamada'])]
            tabela.reset_index(inplace=True, drop=True)
            return tabela
        elif primeira_chamada and not segunda_chamada and nr:
            tabela = tabela[tabela['CHAMADA'].isin(['1ª Chamada','NR'])]
            tabela.reset_index(inplace=True, drop=True)
            return tabela
        elif not primeira_chamada and segunda_chamada and not nr:
            tabela = tabela[tabela['CHAMADA'].isin(['2ª Chamada'])]
            tabela.reset_index(inplace=True, drop=True)
            return tabela
        elif not primeira_chamada and segunda_chamada and nr:
            tabela = tabela[tabela['CHAMADA'].isin(['2ª Chamada','NR'])]
            tabela.reset_index(inplace=True, drop=True)
            return tabela
        elif primeira_chamada and segunda_chamada and nr:
            return tabela
        else:
            tabela = tabela[tabela['CHAMADA'].isin(['NR'])]
            tabela.reset_index(inplace=True, drop=True)
            return tabela
    except:
        return pd.DataFrame()
    
##################################################################################################
def filtra_su(tabela,escolha_su):
    try:
        if 'Geral' == escolha_su:
            return tabela
        elif '1ª Cia Fuz L Mth' == escolha_su:
            tabela = tabela[tabela['COMPANHIA'].isin(['1ª Cia Fuz L Mth'])]
            tabela.reset_index(inplace=True, drop=True)
            return tabela
        elif '2ª Cia Fuz L Mth' == escolha_su:
            tabela = tabela[tabela['COMPANHIA'].isin(['2ª Cia Fuz L Mth'])]
            tabela.reset_index(inplace=True, drop=True)
            return tabela
        elif 'Cia C Ap' == escolha_su:
            tabela = tabela[tabela['COMPANHIA'].isin(['Cia C Ap'])]
            tabela.reset_index(inplace=True, drop=True)
            return tabela
        elif 'CFGS' == escolha_su:
            tabela = tabela[tabela['COMPANHIA'].isin(['CFGS'])]
            tabela.reset_index(inplace=True, drop=True)
            return tabela
        else:
            tabela = tabela[tabela['COMPANHIA'].isin(['B Mus'])]
            tabela.reset_index(inplace=True, drop=True)
            return tabela
    except:
        return pd.DataFrame()

###############################################################################################
def filtra_idade(tabela,escolha_idade=None):
    try:
        if escolha_idade != None:
            if '18-21' == escolha_idade:
                tabela = tabela[(tabela['IDADE']>=18) & (tabela['IDADE']<=21)]
                tabela.reset_index(inplace=True, drop=True)
                return tabela
            elif '22-25' == escolha_idade:
                tabela = tabela[(tabela['IDADE']>=22) & (tabela['IDADE']<=25)]
                tabela.reset_index(inplace=True, drop=True)
                return tabela
            elif '26-29' == escolha_idade:
                tabela = tabela[(tabela['IDADE']>=26) & (tabela['IDADE']<=29)]
                tabela.reset_index(inplace=True, drop=True)
                return tabela
            elif '30-33' == escolha_idade:
                tabela = tabela[(tabela['IDADE']>=30) & (tabela['IDADE']<=33)]
                tabela.reset_index(inplace=True, drop=True)
                return tabela
            elif '34-37' == escolha_idade:
                tabela = tabela[(tabela['IDADE']>=34) & (tabela['IDADE']<=37)]
                tabela.reset_index(inplace=True, drop=True)
                return tabela
            elif '38-41' == escolha_idade:
                tabela = tabela[(tabela['IDADE']>=38) & (tabela['IDADE']<=41)]
                tabela.reset_index(inplace=True, drop=True)
                return tabela
            elif '42-45' == escolha_idade:
                tabela = tabela[(tabela['IDADE']>=42) & (tabela['IDADE']<=45)]
                tabela.reset_index(inplace=True, drop=True)
                return tabela
            elif '46-49' == escolha_idade:
                tabela = tabela[(tabela['IDADE']>=46) & (tabela['IDADE']<=49)]
                tabela.reset_index(inplace=True, drop=True)
                return tabela
            elif 'TODAS' == escolha_idade:
                return tabela
            else:
                tabela = tabela[tabela['IDADE']>=50]
                tabela.reset_index(inplace=True, drop=True)
                return tabela
        else:
            return tabela
    except:
        return tabela
    

################################################################################################
def filtra_pg(tabela,oficiais,st_sgt,cb_sd_ep,sd_ev):
    try:
        if oficiais:
            if st_sgt:
                if cb_sd_ep:
                    if sd_ev:
                        return tabela
                    else:
                        tabela = tabela[tabela['P/G'].isin(['CEL','TEN CEL', 'TC', 'MAJ','CAP','1º TEN','2º TEN','ASP','S TEN','ST','1º SGT','2º SGT','2º SGT QE','3º SGT','CB','SD'])]
                        tabela.reset_index(inplace=True, drop=True)
                        return tabela
                else:
                    if sd_ev:
                        tabela = tabela[tabela['P/G'].isin(['CEL','TEN CEL', 'TC', 'MAJ','CAP','1º TEN','2º TEN','ASP','S TEN','ST','1º SGT','2º SGT','2º SGT QE','3º SGT','SD EV'])]
                        tabela.reset_index(inplace=True, drop=True)
                        return tabela
                    else:
                        tabela = tabela[tabela['P/G'].isin(['CEL','TEN CEL', 'TC', 'MAJ','CAP','1º TEN','2º TEN','ASP','S TEN','ST','1º SGT','2º SGT','2º SGT QE','3º SGT'])]
                        tabela.reset_index(inplace=True, drop=True)
                        return tabela
            else:
                if cb_sd_ep:
                    if sd_ev:
                        tabela = tabela[tabela['P/G'].isin(['CEL','TEN CEL', 'TC', 'MAJ','CAP','1º TEN','2º TEN','ASP','CB','SD','SD EV'])]
                        tabela.reset_index(inplace=True, drop=True)
                        return tabela
                    else:
                        if sd_ev:
                            tabela = tabela[tabela['P/G'].isin(['CEL','TEN CEL', 'TC', 'MAJ','CAP','1º TEN','2º TEN','ASP','CB','SD'])]
                            tabela.reset_index(inplace=True, drop=True)
                            return tabela
                else:
                    if sd_ev:
                        tabela = tabela[tabela['P/G'].isin(['CEL','TEN CEL', 'TC', 'MAJ','CAP','1º TEN','2º TEN','ASP','SD EV'])]
                        tabela.reset_index(inplace=True, drop=True)
                        return tabela
                    else:
                        tabela = tabela[tabela['P/G'].isin(['CEL','TEN CEL', 'TC', 'MAJ','CAP','1º TEN','2º TEN','ASP'])]
                        tabela.reset_index(inplace=True, drop=True)
                        return tabela
        else:
            if st_sgt:
                if cb_sd_ep:
                    if sd_ev:
                        tabela = tabela[tabela['P/G'].isin(['S TEN','ST','1º SGT','2º SGT','2º SGT QE','3º SGT','CB','SD','SD EV'])]
                        tabela.reset_index(inplace=True, drop=True)
                        return tabela
                    else:
                        tabela = tabela[tabela['P/G'].isin(['S TEN','ST','1º SGT','2º SGT','2º SGT QE','3º SGT','CB','SD'])]
                        tabela.reset_index(inplace=True, drop=True)
                        return tabela
                else:
                    if sd_ev:
                        tabela = tabela[tabela['P/G'].isin(['S TEN','ST','1º SGT','2º SGT','2º SGT QE','3º SGT','SD EV'])]
                        tabela.reset_index(inplace=True, drop=True)
                        return tabela
                    else:
                        tabela = tabela[tabela['P/G'].isin(['S TEN','ST','1º SGT','2º SGT','2º SGT QE','3º SGT'])]
                        tabela.reset_index(inplace=True, drop=True)
                        return tabela
            else:
                if cb_sd_ep:
                    if sd_ev:
                        tabela = tabela[tabela['P/G'].isin(['CB','SD','SD EV'])]
                        tabela.reset_index(inplace=True, drop=True)
                        return tabela
                    else:
                        tabela = tabela[tabela['P/G'].isin(['CB','SD'])]
                        tabela.reset_index(inplace=True, drop=True)
                        return tabela
                else:
                    if sd_ev:
                        tabela = tabela[tabela['P/G'].isin(['SD EV'])]
                        tabela.reset_index(inplace=True, drop=True)
                        return tabela
                    else:
                        return pd.DataFrame()
    except:
        pd.DataFrame()


#####################################################################################
#GRAFICO PIZZA
#criando um dicionário de cores para manter a cor fixa para cada menção no gráfico pizza
color_dict = {
    'E': 'Turquoise',
    'MB': 'orange',
    'B': 'green',
    'R': 'brown',
    'I': 'Coral',
    'NR': 'Silver',
    'S': 'Violet'
}
#Função para gráfico pizza
def grafico_pizza(tabela):
    mencao = tabela["MENÇÃO"].value_counts()
    labels,sizes = list(),list()
    for k, v in mencao.items():
        labels.append(k)
        sizes.append(v)
    colors = [color_dict[label] for label in labels]#cria o dicinário para cada cor no labels levantado utilizando o dicionário color_dict
    pizza, ax = plt.subplots() #primeira variável é figura
    #pizza_oficiais.set_facecolor(color='black') #coloca o fundo preto
    #for text in ax.texts: # para colocar a letras na cor branca
        #text.set_color('white')#colocando as letras na cor branca
    ax.pie(
        sizes, #quantidade das menções
        labels=labels,# identificação das menções
        colors=colors,# le o dicionario com as cores pré-definidas
        autopct='%1.1f%%', #para aparecer as porcentagens
        wedgeprops={'width':0.4},# Cria um buraco no fundo do gráfico, fazendo virar um anel
        pctdistance=0.8, #centraliza as porcentagens
        textprops={'fontsize':12, 'weight':'bold'},
        )
    ax.axis('equal')#deixa o gráfico no formato redondo
    ax.text(0,0,f"Menções", ha='center', va='center', fontsize=16, color='black')#coloca o título do gráfico no centro (dois primeiros números dizem respeito a posição)
    return pizza
###################################################3
#FUNÇÃO PARA GRÁFICO DE DISPERSÃO
def grafico_dispersao_mencao(tabela, coluna_quantitativa):
    # Limpar os dados
    df_clean = df.dropna(subset=['MENÇÃO', coluna_quantitativa])
    df_clean[coluna_quantitativa] = pd.to_numeric(df_clean[coluna_quantitativa], errors='coerce')

    # Mapear as menções para valores numéricos para facilitar a visualização
    mencao_map = {'I': 1, 'R': 2, 'S': 3, 'B': 4, 'MB': 5, 'E': 6}
    df_clean['MENÇÃO_NUM'] = df_clean['MENÇÃO'].map(mencao_map)

    # Criar o gráfico
    plt.figure(figsize=(12, 8))
    sns.scatterplot(x=coluna_quantitativa, y='MENÇÃO_NUM', data=df_clean, hue='MENÇÃO', palette='viridis', s=100)

    # Adicionar uma linha de tendência
    sns.regplot(x=coluna_quantitativa, y='MENÇÃO_NUM', data=df_clean, scatter=False, color='red')

    # Configurar o gráfico
    plt.title(f'Relação entre {coluna_quantitativa} e Menção', fontsize=16)
    plt.xlabel(coluna_quantitativa, fontsize=12)
    plt.ylabel('Menção', fontsize=12)
    plt.yticks(range(1, 7), ['I', 'R', 'S', 'B', 'MB', 'E'])

    # Adicionar uma grade
    plt.grid(True, linestyle='--', alpha=0.7)

    # Mostrar o gráfico
    return plt.show()

    # Calcular algumas estatísticas
    # media_var_por_mencao = df_clean.groupby('MENÇÃO')[coluna_quantitativa].mean().sort_values(ascending=False)
    # print(f"Média de {coluna_quantitativa} por menção:")
    # print(media_var_por_mencao)

    # correlacao = df_clean[coluna_quantitativa].corr(df_clean['MENÇÃO_NUM'])
    # print(f"\nCorrelação entre {coluna_quantitativa} e Menção: {correlacao:.2f}")





######### INICIANDO A CRIAÇÃO DA PÁGINA
#TÍTULO
st.markdown("<h1 style='text-align: center;'>TAF 2024 - 10º BIL Mth</h1>", unsafe_allow_html=True)

######CRIANDO A MOLDURA DOS BOTÕES DO TAF
with st.container(border=True):
    col1,col2,col3 = st.columns(3) #cria 3 colunas
    taf_1 = col1.checkbox('1º TAF',value=True)
    taf_2 = col2.checkbox('2º TAF')
    taf_3 = col3.checkbox('3º TAF')

tabela_do_taf = pega_taf(tabela_tafs,taf_1,taf_2,taf_3)#pegando os taf selecionados

col_central = st.columns([1, 4, 1])[1] #criando as colunas

col4, mid_col, col7 = st.columns([0.15,0.7,0.15], vertical_alignment='center')
col5,col6 = mid_col.columns(2, vertical_alignment='center')
with col4:
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

    #lista_itens = ['TODOS', 'IDADE', 'CORRIDA', 'FLEXÃO', 'ABDOMINAL','BARRA', 'MENÇÃO']
    #escolha_itens = st.radio('ITENS PARA CONSULTA', lista_itens, index=1,label_visibility='hidden')
    
    st.subheader('CHAMADAS')
    primeira_chamada = st.checkbox('1ª Chamada',value=True)
    segunda_chamada = st.checkbox('2ª Chamada',value=True)
    nr = st.checkbox('Não Realizado')
    
with col7:
    lista_su = ['Geral','1ª Cia Fuz L Mth', '2ª Cia Fuz L Mth','Cia C Ap', 'CFGS','B Mus']
    st.subheader('SUBUNIDADES')
    escolha_su = st.radio('**SUBUNIDADES**', options=lista_su, index=1, label_visibility='hidden')
    st.subheader('POSTOS E GRADUAÇÕES')
    oficiais = st.checkbox('Oficiais',value=True)
    st_sgt = st.checkbox('ST e Sgt')
    cb_sd_ep = st.checkbox('Cb/Sd EP')
    sd_ev = st.checkbox('Sd EV')

tabela_filtrada =(filtra_su(
    filtra_pg(
        filtra_chamadas(
            pega_taf(tabela_tafs,taf_1,taf_2,taf_3)
        ,primeira_chamada,segunda_chamada,nr)
    ,oficiais,st_sgt,cb_sd_ep,sd_ev)
,escolha_su)
)

tabela_filtrada_idade = filtra_idade(tabela_filtrada,escolha_idade)
tabela_filtrada_idade

if idade:
    if corrida:
        if flexao:
            if abdominal:
                if barra:
                    if mencao:#Todos os itens
                        with mid_col:
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
                            st.pyplot(grafico_pizza(tabela_filtrada))
                        with col6:
                            st.dataframe(tabela_filtrada.drop(columns=['OBS', 'COMPANHIA', 'CHAMADA','TAF','BI Publicado','CORRIDA','BARRA','ABDOMINAL','FLEXÃO']))
                    else:#(tudo desmarcado)
                        with mid_col:
                            st.dataframe(tabela_filtrada_idade)


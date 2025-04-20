import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import pandas as pd


def determinar_mencao(idade,dicio_atividades,atividade,lem,segmento,indice):# retorna a menção correta para o índice indicado
    '''segmento - retirado da coluna 'SEGMENTO' da tabela
       idade - retirado da coluna "IDADE" da tabela
       atividade - nome da coluna da atividade na tabela
       desempenho - item retirado da coluna da atividade
       lem - retirado da coluna "LEM"
    '''
    if idade == None or isinstance(idade,str) or idade < 18:
        return 'erro idade'

    if segmento not in ['M','F'] or segmento == None:
        return 'erro no segmento'

    if lem not in ['B','CT'] or lem == None:
        return 'erro na LEM'

    if indice == None:
        return f'erro no indice - {atividade}'

    if isinstance(indice,str):
        if indice == 'NR' or indice == 'A':
            return indice
        else:
            return f'erro no indice - {atividade}'
    #indice = int(indice)

# determinar a faixa de idade
    if lem == 'B':
            for faixa in dicio_atividades[lem][atividade][segmento].keys():
                inicio, fim = map(int, faixa.split('-'))
                if inicio <= idade <= fim:
                    faixa = faixa
                    break
    else:
        if atividade == 'BARRA':
            faixa = 'X'
        else:
            for faixa in dicio_atividades[lem][atividade][segmento].keys():
                inicio, fim = map(int, faixa.split('-'))
                if inicio <= idade <= fim:
                    faixa = faixa
                    break

#determinar a menção
    if faixa != 'X':
        for f in dicio_atividades[lem][atividade][segmento].keys():
            if f == faixa:
                dicio_mencoes = dicio_atividades[lem][atividade][segmento][f]
                if isinstance(dicio_mencoes, dict):
                    for k, (min,max) in dicio_mencoes.items():
                        if min <= indice <= max:
                            return k
                else:
                    if indice >= dicio_mencoes:
                        return "S"
                    else:
                        return "I"
    else:
        return indice

##########################->FILTROS PARA A TABELA<-###############################
#ESSAS FUNÇÕES ESTÃO DIRETAMENTE DEPENDENTES DOS BOTAÕES DE SELEÇÃO DO PROGRAMA PRINCIPAL
#POR ISSO TEM QUE SER COLOCADAS DEPOIS DAS SELEÇÕES

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

##################################################################################
def filtra_segmento(tabela, segmento, mas, fem):
    try:
        if segmento:
            if mas and not fem:
                tabela = tabela[tabela['SEGMENTO'].isin(['M'])]
                tabela.reset_index(inplace=True,drop=True)
                return tabela
            elif not mas and fem:
                tabela = tabela[tabela['SEGMENTO'].isin(['F'])]
                tabela.reset_index(inplace=True,drop=True)
                return tabela
            else:
                return tabela
        else:
            return tabela
    except:
        return tabela


####################-> GRÁFICOS <-#####################

#Gráfico Pizza para as menções
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
def grafico_pizza(tabela, info):
    try:
        info_tab = tabela[info].value_counts()
        labels,sizes = list(),list()
        for k, v in info_tab.items():
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
        ax.text(0,0, info, ha='center', va='center', fontsize=16, color='black')#coloca o título do gráfico no centro (dois primeiros números dizem respeito a posição)
        return pizza
    except:
        return "Erro na geração do gráfico: verifique os dados lançados na planilha."


###### Gráfico de barra para representar a quantidade de militares na quantidade do indice alcançado na atividade
def para_um(tabela, atividade):
    tabela = tabela[~((tabela[atividade] == 'A') | (tabela[atividade].isna()) | (tabela[atividade] == 'X'))]# trata a tabela para tirar "A", nulo e 'X'
    df_mencao_count = tabela[atividade].value_counts().reset_index()
    df_mencao_count.columns = [atividade, "count"]
    fig_bar_mencao = px.bar(
    df_mencao_count, 
    x= atividade, 
    y="count", 
    title=f"Quantidade de Militares X Quantidade de {atividade}",
    labels={atividade: f'Quantidade de {atividade}', "count": "Quantidade de Militares"}
    )
    st.plotly_chart(fig_bar_mencao)

####Gráfico de disperção para uma atividade, levando em consideração a idade e o segmento
def idade_seg_atv(tabela, atividade):
    tabela = tabela[~((tabela[atividade] == 'A') | (tabela[atividade].isna()) | (tabela[atividade] == 'X'))] # trata a tabela para tirar "A", nulo e 'X'
    try:
        cores_personalizadas = ['#377eb8','#e41a1c']
        media_atividade = tabela[atividade].mean()
        fig_scatter = px.scatter(tabela, 
                                x="IDADE", 
                                y= atividade,
                                color="SEGMENTO",
                                color_discrete_sequence=cores_personalizadas,
                                hover_data=["NOME", "P/G"],
                                title=f"Desempenho na(o) {atividade} por SEGMENTO E IDADE")
        fig_scatter.add_hline(
        y=media_atividade,
        line_dash="dash",
        line_color="red",
        annotation_text=f"Média: {media_atividade:.2f}",
        annotation_position="top right"
    )
        st.plotly_chart(fig_scatter)
    except:
        st.write(f"Ocorreu um erro, provavelmente a coluna {atividade} está com algum valor lançado errado. Verifique a tabela abaixo e tente identificar e corrigir.")




#somente para realização de testes
if __name__=='__main__':
    from pathlib import Path
    from tabela_indice import *
    diretorio_atual = Path.cwd()
    arquivo = diretorio_atual/'PLANILHA TAF.xlsx'
    arquivo_excel = pd.ExcelFile(arquivo)#variável recebe todo o arquivo exel com suas abas
    dfs = [pd.read_excel(arquivo_excel,sheet_name=sheet).assign(TAF=sheet) for sheet in arquivo_excel.sheet_names] #cria uma lista com as abas da planilha
    tabela_tafs = pd.concat(dfs,ignore_index=True)#concatena as abas da planilha em uma só

    #tabela_tafs = tabela_tafs[~((tabela_tafs["CORRIDA"] == 'A') | (tabela_tafs["CORRIDA"].isna()) | (tabela_tafs["CORRIDA"] == 'X'))] # trata a tabela para tirar "A", nulo e 'X'
    tabela_tafs["menção item"] = tabela_tafs.apply(lambda row: determinar_mencao(row['IDADE'],dicio_atividades,'CORRIDA', row['LEM'], row['SEGMENTO'], row['CORRIDA']), axis=1)
    #idade,dicio_atividades,atividade,lem,segmento,indice
    a = tabela_tafs['menção item'].value_counts()
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 22:14:49 2019

@author: gustavo.fonseca
"""
import matplotlib.pyplot as plt
import pandas as pd

#Tarefa 10 exercício

'''Esta tarefa envolve o uso de dados de tabelas para a resolução dos exercícios.
Cada teste será explicado para o fácil entendimento. As tabelas utilizadas serão
extraídas da pasta "Downloads" do computador do usuário (gustavo.fonseca), mas 
podem ser obtidas na página da tarefa para a execução em outros computadores.'''

#Exercício 1:Futebol
'''Esse exercício envolve o placar dos jogos do campeonato Brasileiro de futebol de 
2018. Estaremos definindo a porcentagem de vitórias e não derrotas do time 
mandante (da casa).'''
tab1 = pd.read_csv('file:///C:/Users/gustavo.fonseca/Downloads/tabelaBrasileirao2018.csv')
x=tab1['Placar do Mandante'].values
y=tab1['Placar do Visitante'].values
v=(len(x[x>y]))#Valor do número de vitórias do time do mandante.
nd=(len(x[x>=y]))#Valor do número de não derrotas do time do mandante.
print('Exercício 1:')
print('O time mandante ganhou',v,'jogos, o que equivale a',round((v*100)/380,2),'% dos jogos.')#Utilizaremos uma regra de 3 básica para definir a porcentagem.
print('O time mandante não perdeu',nd,'jogos, o que equivale a',round((nd*100)/380,2),'% dos jogos.')



print()
#Exercício 2: Inflação

'''Neste exercício, estaremos analisando a tabela da taxa de inflação mensal no Brasil
de fevereiro de 1944 a junho de 2019. Plotaremos um gráfico da inflação em relação
ao tempo e definiremos a maior taxa de inflação presente no gráfico.'''
tab2=pd.read_csv('file:///C:/Users/gustavo.fonseca/Downloads/inflacaoMensal.csv')
tab2['Tempo']=tab2['Ano']+(tab2['Mês']/12)#Coluna representando o tempo em anos+meses/12.
i=tab2.sort_values(['Inflação'])#Tabela em ordem ascendente de inflação.
print('Exercício 2:')
plt.figure
plt.plot(tab2['Tempo'],tab2['Inflação']) 
plt.title('Gráfico Exercício 2')
plt.xlabel('Tempo')
plt.ylabel('Taxa de Inflação')
plt.show 
print('O mês e ano com a maior inflação apresentada:')
print()
print(i.tail(1))#Último elemento da tabela i, que representa a maior inflação.
print()
print('ou seja, março de 1990, com uma taxa de inflação de 81.32.')
 
 
 
print()
 #Exercício 3: Netflix
 
'''Nesse teste analisaremos um histórico de visualização do Netflix, para definir
os 10 programas mais vistos e em qual mês do ano foi assistido mais programas.'''
tab3=pd.read_csv('file:///C:/Users/gustavo.fonseca/Downloads/netflix.csv')

tab3['Categoria'] = 'Filme'  
tab3['Categoria'][tab3['Title'].str.contains(": Temporada|: Stranger|: Parte")] = 'Série'  
tab3['Programa'] = tab3['Title']  
tab3[['Programa','Episódio']] = tab3[tab3['Categoria']=='Série']['Title'].str.split(pat = ': Temporada|: Stranger Things|: Parte', expand = True, n = 1)   
tab3.loc[tab3['Categoria']=='Filme', 'Programa'] = tab3.loc[tab3['Categoria']=='Filme', 'Title'] #Comando sugerido pelo professor para facilitar a execução do exercício. 
tab3['Date'] = pd.to_datetime(tab3['Date'], format = '%d/%m/%Y')
p=tab3['Programa'].value_counts()#Tabela representando a quantidade de espisódios assistidos de cada programa.
d=tab3['Date'].dt.month.value_counts()#Tabela representando a quantidade de programas assistidos em cada mês do ano.
print('Exercício 3:')
print('As séries mais assistidas foram:')
print(p.head(10))#Primeiros 10 elementos da tabela p, representando os 10 programas mais assistidos.
print()
print('Foram assistidos mais programas no mês:')
print(d.head(1))#Primeiro elemento da tabela d, representando o mês do ano em que foram assistidos mais programas.
print('ou seja, em novembro.')
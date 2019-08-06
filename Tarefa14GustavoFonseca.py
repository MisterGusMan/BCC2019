# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 16:36:55 2019

@author: gustavo.fonseca
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Tarefa 14 

'''Essa tarefa envolve o uso de conceitos estatísticos para a resolução dos testes.
Alguns exercícios serão baseados em tabelas, que podem ser encontradas na página 
da tarefa.'''

#Exercício 1:Torque

'''Estaremos plotando o gráfico da o gráfico do torque na direção y (Nm) 
em função do tempo (s). Além disso, calcularemos a média e o desvio-padrão
do torque na direção y.'''

print('Exercício 1:')

t=pd.read_csv('file:///C:/Users/gustavo.fonseca/Downloads/balance.csv')
t2=pd.DataFrame()#Nova tabela incluindo apenas o torque na direção y e o tempo. 
t2['Tempo']=t['Time[s]']
t2['Torque y']=t['My[Nm]']
w=t2['Torque y']
plt.figure()
plt.plot(t2['Tempo'],w)
plt.plot(np.linspace(0,60,6),np.mean(w)*np.ones((6)),color='r',label='Média')
plt.plot(np.linspace(0,60,6),(np.mean(w)+w.std())*np.ones((6)),color='g',linestyle='--',label='Desvio-padrão')
plt.plot(np.linspace(0,60,6),(np.mean(w)-w.std())*np.ones((6)),color='g',linestyle='--')
#Os três comandos acima foram usados para plotar a média e o desvio-padrão no gráfico.
plt.title('Gráfico Exercício 1')
plt.xlabel('Tempo(s)')
plt.ylabel('Torque na direção y(Nm)')
plt.legend()
plt.show()

print('A média do torque na direção y é',np.mean(w),'Nm','e seu desvio padrão é',w.std(),'Nm.')

print()

#Exercício 2:Inflação

'''Usaremos a tabela com a  taxa de inflação mensal no Brasil de fevereiro de 
1944 a junho de 2019 para calcular vários valores estatísticos, além de plotar
o histograma da inflação mensal nos meses de março.'''

print('Exercício 2:')

i=pd.read_csv('file:///C:/Users/gustavo.fonseca/Downloads/inflacaoMensal.csv')
i2=i[i['Mês']==3]#Nova tabela incluindo somente os meses de março.
z=i2['Inflação']
print('A mediana da inflação mensal nos meses de março foi',np.median(z),'%.')
print('A média da inflação mensal nos meses de março foi',np.mean(z),'%.')
print('O desvio-padrão da inflação mensal nos meses de março foi',z.std(),'%.')
plt.figure()
plt.hist(z,76,color='orange')
plt.plot(np.mean(z)*np.ones((5)),np.linspace(0,22,5),color='r',label='Média')
plt.plot(np.median(z)*np.ones((5)),np.linspace(0,22,5),color='b',label='Mediana')
plt.title('Gráfico Exercício 2')
plt.xlabel('Inflação nos meses de março(%)')
plt.legend()
plt.show()

print()

#Exercício 3:Inflação (2)

'''Este exercício é uma cópia do anterior, mudando apenas a data da coleta dos
dados (a partir de 1995). Estaremos também comentando a razão da diferença 
entre a média e a mediana ser alta no segundo item e baixa no terceiro item do
exercício.'''
 
print('Exercício 3:')

c=pd.read_csv('file:///C:/Users/gustavo.fonseca/Downloads/inflacaoMensal.csv')
c2=i[np.logical_and(i['Mês']==3,i['Ano']>=1995)]#Nova tabela incluindo somente os meses de março a partir de 1995.
y=c2['Inflação']
print('A mediana da inflação mensal nos meses de março a partir de 1995 foi',np.median(y),'%.')
print('A média da inflação mensal nos meses de março a partir de 1995 foi',np.mean(y),'%.')
print('O desvio-padrão da inflação mensal nos meses de março a partir de 1995 foi',y.std(),'%.') 
plt.figure()
plt.hist(y,25,color='cyan')
plt.plot(np.mean(y)*np.ones((9)),np.linspace(0,4,9),color='r',label='Média')
plt.plot(np.median(y)*np.ones((9)),np.linspace(0,4,9),color='b',label='Mediana')
plt.title('Gráfico Exercício 3')
plt.xlabel('Inflação nos meses de março a partir de 1995(%)')
plt.legend()
plt.show()

'''A diferença entre a média e a mediana ser alta no segundo item e baixa no 
terceiro item se dá pela retirada dos 51 valores correspondentes ao período 
1945-1995. A inflação mensal nesse período apresenta certos valores 
significativamente maiores do que a maioria (conhecidos como "outliers"). 
A presença desses valores aumenta a diferença entre a média e a mediana no 
segundo item, enquanto a sua retirada torna os valores mais parecidos no 
terceiro item.'''
 
print()
 
#Exercício 4:Números Aleatórios 
 
'''Usaremos o comando 'np.random.rand(N)' para gerar N números aleatórios
entre 0 e 1, para depois gerar um histograma e calcular a média dos valores 
gerados. Faremos isso para  N = 100, N = 1000, N = 10000 e N = 100000.'''
 
print('Exercício 4:')

for N in np.array([100,1000,10000,100000]):#Usaremos o "for" para simplificar o cálculo para os múltiplos valores de N.
    x=np.random.rand(N)
    print('A média para N=',N,'é',np.mean(x))
    plt.figure()
    plt.hist(x,color='g')
    plt.plot(np.mean(x)*np.ones((7)),np.linspace(0,N/10,7),color='r',label='Média')
    plt.title('Gráfico Exercício 4')
    plt.legend()
    plt.show
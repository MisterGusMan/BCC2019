# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 16:37:20 2019

@author: gustavo.fonseca
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Tarefa 12

'''Nessa tarefa, estaremos utilizando estruturas de repetição pata determinar 
diversos valores. Cada exercício e fórmula sera explicado nos comentários.'''

#Exercício 1: Valor de pi

'''Neste exercício, estaremos usando a fórmula de Leibniz para encontrar o valor
aproximado de pi. A fórmula a ser utilizada é 4-(4/3)+(4/5)-(4/7)+(4/9)+... .
Calcularmos o valor aproximado de pi para 50, 500, 1000 e 10.000 termos.'''
print('Exercício 1')
p=0
for i in range(10001): #Os números de todos os testes estão nesta range, simplificando a tarefa.
    p=p+(-1)**i/(2*i+1) #Estaremos utilizando uma forma simplificada da fórmula, fatorando o 4 no numerador da somatória, tornando-o igual à -1^i.
    π=4 * p #Multiplicaremos o resultado por 4 pelo fator de 4 antes retirado.
    if i == 50:
        print('a)Para N=',i,'temos π=',π)
    if i == 500:
        print('b)Para N=',i,'temos π=',π)
    if i == 1000:
        print('c)Para N=',i,'temos π=',π)
    if i == 10000:
        print('d)Para N=',i,'temos π=',π)

print()    

#Exercício 2: Inflação
'''Neste exercício, estaremos plotando um gráfico com a taxa de inflação anual 
entre 1945 e 2018, com os dados fornecidos por um DataFrame. Tal arquivo será
extraído da pasta 'Downloads' do usuário, e está disponível na página da tarefa.'''

i=pd.read_csv('file:///C:/Users/gustavo.fonseca/Downloads/inflacaoMensal.csv')
i2=i[np.logical_and(i['Ano']>=1945,i['Ano']<=2018)]#Tabela com os anos entre 1945 e 2018.
inf=1 
a2=i2['Inflação']
a=i2['Ano']
for i in i2.loc[np.arange(11,23),'Inflação'].values:
      inf=inf*(1+i/100)
print((inf-1)*100)

plt.figure()
plt.plot(a,a2)
plt.title('Gráfico exercício 2')
plt.xlabel('Tempo(anos)')
plt.ylabel('Taxa de inflação(%)')
plt.show()


#Exercício 3: Onda Quadrada
'''Neste exercício, estaremos utilizando a série de Fourier para calcular a 
aproximação de uma onda quadrada. Tal série é definida como:x(t)≈(4/π)*∑(i=1 N)sin[(2i-1)t]/2i-1.
Estaremos plotando os gráficos para N=10, N=100, N=1000 e N=10.000'''


t=np.linspace(0,11,10000)
s=0
for i in range (1,10001):
    s=s+(np.sin(((2*i)-1)*t)/(2*i)-1)
    x=(4/np.pi)*s
    if i == 10:
        x1=x
    if i == 100:   
        x2=x
    if i == 1000:
        x3=x
    if i == 10000: 
        x4=x
plt.figure()
plt.plot(t,x)
plt.plot(t,x2)
plt.plot(t,x3)
plt.plot(t,x4)
plt.title('Gráfico exercício 3')
plt.xlabel('Tempo(s)')
plt.ylabel('Aproximação da onda')
plt.show()




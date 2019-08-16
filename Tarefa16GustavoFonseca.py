# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:26:00 2019

@author: gustavo.fonseca
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#Tarefa 16

#Exercício 1:
print('Exercício 1) (Respostas nos gráficos).')
def Funçãoxt(t,b,A,c):
    '''
    Esta função tem como objetivo a determinação de um valor x em relação a t,A,
    b e c, além de plotar o gráfico da relação x x t.
    ---------------------------------------------------------------------------
    Parâmetros:
    ...........................................................................    
        A,b e c: 
            Valores reais que definem as variáveis da função.
        t:
            Vetor definido por um intervalo entre dois números reais.
    ---------------------------------------------------------------------------        
    Retorna:
    ........................................................................... 
         x:
             Vetor definido Vetor definido por um intervalo entre dois números 
             reais, plotado em um gráfico x x t.
             
      '''
    x=A*(np.sqrt(1+b*t**2))+c
    plt.figure()
    plt.plot(t,x)
    plt.title('Gráfico Exercício 1')
    plt.xlabel('t')
    plt.ylabel('x')
    plt.grid()
    plt.show()
    return x

#Teste 1:
A1 = 2 
b1 = 0.5 
c1 = 0 
t1 = np.linspace(0,10,1000) 
x1 = Funçãoxt(t1,b1,A1,c1)

#Teste 2:
A2 = 10
b2 = 0.2 
c2 = 1 
t2 = np.arange(0,15.2,0.2) 
x2 = Funçãoxt(t2,b2,A2,c2)

#Teste 3:
A3 = -3
b3 = -1.5
c3 = -10
t3 = np.linspace(-0.5,0.5,500) 
x3 = Funçãoxt(t3,b3,A3,c3)

print()

#Exercício 2:
print('Exercício 2)')
def CaraOuCoroa(n):
    '''
    Esta função tem como objetivo a simulação de um lançamento de uma moeda, com
    50% de chance de obter uma cara ou uma coroa.
    ---------------------------------------------------------------------------
    Parâmetros:
    ...........................................................................
         n:
             número de vezes que a "moeda" será lançada.
    ---------------------------------------------------------------------------
    Retorna:
    ...........................................................................  
        Resposta=boolean:
             A resposta possui 50% de chance de ser cara ou coroa.
     '''
    z=0
    y=0
    for x in np.random.rand(n):
        if x < 0.5: 
            resposta='Cara'
            z+=1
        else:
            resposta='Coroa'
            y+=1
        print(resposta)
    print('Você obteve',z,'caras e',y,'coroas.')
    return resposta
resposta=CaraOuCoroa(10)#Testaremos a função 10 vezes.

print()    
         
#Exercício 3:
print('Exercício 3)')
def Moda(DF,N):
    '''
    Esta função define a moda de uma coluna de um DataFrame do Pandas.
    ---------------------------------------------------------------------------
    Parâmetros:
    ...........................................................................    
        DF:
            DataFrame escolhido convertido pelo Pandas .
        N:
            Nome da coluna do DataFrame escolhido.
    ---------------------------------------------------------------------------
    Retorna:
    ...........................................................................    
        Moda:
            O elemento mais presente nas amostras da coluna escolhida.
     '''   
    d=DF[N]
    d2=d.value_counts()
    Moda=d2.index[0]
    print('A moda da coluna',N,'é o elemento',Moda)
    return Moda
#Teste com a coluna dos estádios do Campeonato Brasileiro
DF1=pd.read_csv('file:///C:/Users/gustavo.fonseca/Downloads/tabelaBrasileirao2018.csv')    
N1='Estádio'    
moda1=Moda(DF1,N1)    


print()    

#Exercício 4:
print('Exercício 4)')
def InclinaçãoDaReta(x1,y1,x2,y2,N):  
    '''
    Função que determina a inclinação da reta m e o ponto b em que a reta 
    cruza o eixo y da reta y=mx+b que passa pelos dois pontos. Além disso plota o
    gráfico da reta encontrada com N pontos, mostrando os dois pontos dados como 
    entrada, indicados com marcadores quadrados.
    ---------------------------------------------------------------------------
    Parâmetros:
    ...........................................................................    
        x1,y1,x2 e y2:
            Valores das coordenadas (x1,y1) e (x2,y2) de dois pontos.
        N:
            Número de pontos no gráfico da reta.
    ---------------------------------------------------------------------------        
    Retorna:
    ........................................................................... 
        m:
            Inclinação da reta plotada.
        b:
            Ponto em que a reta cruza o eixo y da reta y=mx+b que passa pelos dois pontos.
    
    '''
    m=(y2-y1)/(x2-x1)
    b=y1-m*x1
    print('A inclinação da reta que passa pelos pontos',(x1,y1),'e',(x2,y2),'é igual a',m,'e o seu ponto b é igual a',b)
    print()
    plt.figure()
    plt.plot(np.linspace(x1,x2,N),np.linspace(y1,y2,N),color='r')
    plt.plot(x1,y1,marker='s',label='Ponto 1')
    plt.plot(x2,y2,marker='s',label='Ponto 2')
    plt.plot(0,b,marker='d',label='Ponto b')
    plt.title('Gráfico Exercício 4')
    plt.grid()
    plt.legend()
    plt.show()
    
    return m,b

#Teste 1:
x1a = -19 
y1a = 2 
x2a = 10 
y2a= -10
Na=1000
xa = InclinaçãoDaReta(x1a,y1a,x2a,y2a,Na)

#Teste 2:
x1b = -2
y1b = 8
x2b = 20
y2b = 43
Nb = 2000
xb = InclinaçãoDaReta(x1b,y1b,x2b,y2b,Nb)   
    
#Teste 3:
x1c = 7
y1c = 13 
x2c = 1 
y2c = 2 
Nc = 500    
xc = InclinaçãoDaReta(x1c,y1c,x2c,y2c,Nc)    
    
    
    
    
    
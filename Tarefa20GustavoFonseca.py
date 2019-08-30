# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 21:09:05 2019

@author: gustavo.fonseca
"""
import numpy as np
import matplotlib.pyplot as plt

#Tarefa 20:
α=0.01
β=0.001 
δ=0.007 
γ=0.000009
'''Os valores dos parâmetros foram modificados para funcionar com o período de 
tempo (0.01 dias por instante)'''
C=np.zeros((100000))
R=np.zeros((100000))
'''Definiremos R e C como vetores com 10^5 elementos para plotar o gráfico de 1000
dias pedido no exercício'''
C[0]=1000
R[0]=12
for i in range (1,len(C)):
     C[i]=C[i-1]+(α*C[i-1]-β*C[i-1]*R[i-1])*0.01
     R[i]=R[i-1]+(γ*R[i-1]*C[i-1]-δ*R[i-1])*0.01
plt.subplot(2,1,1)
plt.plot(C) 
plt.title('Variação de Coelhos e Raposas')
plt.ylabel('Quantidade de Coelhos')
plt.grid()
plt.subplot(2,1,2)
plt.plot(R)  
plt.ylabel('Quantidade de Raposas')
plt.xlabel('Tempo(1000 dias * 10²)') 
plt.grid()
plt.show() 
print('O valor máximo de coelhos no intervalo de tempo foi',np.max(C),'e o mínimo foi',np.min(C))
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 19:06:37 2019

@author: gustavo.fonseca
"""
import numpy as np
import matplotlib.pyplot as plt

#Tarefa 11
'''Nesta tarefa, estaremos calculando os primeiros 250 valores de três séries,
e iremos plotar um gráfico relacionando os resultados.'''

v=np.zeros((250))#Definiremos v,y e t como vetores de 250 elementos.
y=np.zeros((250))
t=np.zeros((250))
v[0]=10
y[0]=0
t[0]=0 
for i in range(1,len(v)):
 v[i]= v[i-1]+0.01*(-9.81)
for i in range(1,len(v)):
 y[i]= y[i-1]+0.01*v[i-1]
for i in range(1,len(v)):
 t[i]= t[i-1]+0.01

print('Primeiros 250 valores de v:',v)
print()
print('Primeiros 250 valores de y:',y)
print()
print('Primeiros 250 valores de t:',t)

plt.subplot(2, 1, 1)
plt.plot(t,y)
plt.title('Gráficos (t x y) e (t x v)')
plt.ylabel('Altura(m)')
plt.subplot(2, 1, 2)
plt.plot(t,v,color='r',linestyle='--')
plt.xlabel('Tempo(s)')
plt.ylabel('Velocidade(m/s)')
plt.show


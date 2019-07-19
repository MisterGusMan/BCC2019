# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 20:05:05 2019

@author: gustavo.fonseca
"""
import pandas as pd
import matplotlib.pyplot as plt

'''Essa tarefa envolve a plotagem de um gráfico da taxa de analfabetismo em
São Paulo em função do tempo. Tal gráfico será baseado no arquivo CSV mostrado
no exercício.'''
A=pd.read_csv('file:///C:/Users/gustavo.fonseca/Downloads/analfabetismo.csv')
y=A['São Paulo']#Função que cria um arranjo dos valores específicos da coluna "São Paulo"'''
x=A['Ano']#Função que cria um arranjo dos valores específicos da coluna "Ano"'''
plt.figure
plt.plot(x,y,marker='o',markersize=4)
plt.title('Gráfico tarefa 9')
plt.xlabel('Tempo(Anos)')
plt.ylabel('Taxa de Analfabetismo em São Paulo')
plt.grid()
plt.show
print(A)
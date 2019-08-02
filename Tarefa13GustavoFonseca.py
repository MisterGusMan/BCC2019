# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 19:12:53 2019

@author: gustavo.fonseca
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Tarefa 13

'''Nesta tarefa, criaremos um histograma do público para um time específico do 
Campeonato Brasileiro de Futebol de 2018, baseado no DataFrame disponível na 
página da tarefa. Além disso,estaremos calculando a média desse público, 
baseado no mesmo DataFrame.'''

t=pd.read_csv('file:///C:/Users/gustavo.fonseca/Downloads/tabelaBrasileirao2018.csv')
t2=pd.DataFrame()#Tabela simplificada para o time mandante e o público dos jogos.
t2['Time'] = t['Mandante']
t2['Público'] = t['Público']
t3=t2[t2['Time']=='Palmeiras']#O time usado como referência é o Palmeiras.
x=t3['Público']
plt.figure()
plt.hist(x)
plt.xlabel('Público')
plt.title('Gráfico Tarefa 13')
plt.show()
print('O público médio presente nos jogos em que o Palmeiras foi mandante foi',np.mean(x),'pessoas.')
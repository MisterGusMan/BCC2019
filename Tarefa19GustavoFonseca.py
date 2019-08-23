# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 18:57:09 2019

@author: gustavo.fonseca
"""

import numpy as np

#Tarefa 19:

x,y=[np.random.rand(1000000),np.random.rand(1000000)]
#Definiremos 1000000 pontos [x,y] entre o intervalo [0,1].

d=np.sqrt((0.5-x)**2+((0.5-y)**2))
#Distância entre os pontos e o centro da circunferência.

print('Pi é aproximadamente igual a',4*(len(d[d<=0.5])/1000000))

'''Como pi é igual a 4*(número de pontos dentro do círculo/total de pontos),ele 
pode ser encontrado ao dividir a quantidade de pontos aleatórios cuja distância
ao centro é menor ou igual ao raio do círculo (0.5) pelo total de pontos(1000000).'''
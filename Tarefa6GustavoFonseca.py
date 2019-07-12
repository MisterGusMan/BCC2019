# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 16:10:11 2019

@author: gustavo.fonseca
"""

#Tarefa 6 
'''Esse script foi criado para a resolução dos exercícios da tarefa 6. Várias
fórmulas serão utilizadas na resolução, e serão explicadas nos comentários.
As soluções serão plotadas em gráficos, que serão titulados para a melhor
identificação e entendimento.'''
import numpy as np
import matplotlib.pyplot as plt


#Exercício 1: Tensão elétrica em um circuito.

'''Nesse exercício, etaremos calculando a tensão elétrica medida em um circuito,
em relação ao tempo. Com "v" representando a voltagem e "t" o tempo, 
temos v(t)=np.exp(-0.5*t)*np.cos(2*np.pi*0.8*t).'''
 
t=np.arange(0, 10, 0.05)#Tempo entre 0 e 10 segundos, com incrementos de 0.05s.
v=np.exp(-0.5 *t)*np.cos( 2 * np.pi * 0.8 * t)
plt.figure()
plt.plot(t,v,color='navy')
plt.title('Gráfico exercício 1')
plt.xlabel('Tempo(s)')
plt.ylabel('Voltagem(v)')
plt.show()


#Exercício 2:Temperatura em Fahrenheit e Celsius.

'''Nesse exercício, estaremos determinando a temperatura em fahrenheit em 
relação a uma temperatura em celsius. A fórmula usada para essa conversão é 
f(c)=((9/5)*c)+32, com "f" representando fahrenheits(oF) e "c" celsius(oC).'''

c=np.linspace(-20,100,100)#Temperatura variando de -20 a 100oC,dividido em 100 partes.
f=((9/5)*c)+32
plt.figure()
plt.plot(c,f,color='green',linestyle='-.')
plt.title('Gráfico exercício 2')
plt.xlabel('Temperatura em Celsius(oC)')
plt.ylabel('Temperatura em Fahrenheit(oF)')
plt.show()


#Exercício 3:População de uma cidade.
'''Esse exercício pede a determinação da população de uma cidade em relação ao
tempo, com o número de pessoas crescendo proporcionalmente a fórmula
p(a)=800000*np.exp((a-1994)/40), com "p" representando a população em pessoas e 
"a" representando o ano escolhido'''

#Teste a) 
a=np.arange(1994,2020)#Intervalo de tempo entre 1994 e 2020.
p=800000*np.exp((a-1994)/40)
plt.figure()
plt.plot(a,p,color='red',linestyle='--')
plt.title('Gráfico exercício 3')
plt.xlabel('Ano')
plt.ylabel('População')
plt.show()

#Teste b)
print('Esta cidade terá aproximadamente',int(np.ceil(800000*np.exp((2020-1994)/40))),'habitantes em 2020.')
'''Usamos a função int() para inteirar o número de pessoas na cidade,
já que o mesmo não pode ser decimal.'''
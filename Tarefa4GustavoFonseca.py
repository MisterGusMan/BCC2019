# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 20:05:10 2019

@author: gustavo.fonseca
"""

'''Esse é um script criado para a resolução da tarefa 4. Cada exercício usará 
fórmulas diferentes,que serão explicadas nos comentários.'''
import numpy as np

#------------------------------------------------------------------------------

#Exercício 1: Volume de uma esfera.

'''A fórmula usada nesse exercício é
V=(4*π*(R**3))/3, com R igual ao raio da esfera.'''

print("Exercício 1:")

#Teste a)
R=0.32#m
V=(4*np.pi*(R**3))/3
print("a.Volume=",round(V,2),"m³")

#Teste b)
R=1#m
V=(4*np.pi*(R**3))/3
print("b.Volume=",round(V,2),"m³")

#Teste c)
R=1.9#m
V=(4*np.pi*(R**3))/3
print("c.Volume=",round(V,2),"m³")

#------------------------------------------------------------------------------

#Exercício 2: Temperatura em Fahrenheit.

'''Nesse exercício,estaremos convertendo temperaturas em graus Celsius para 
graus Fahrenheit. A fórmula usada para essa conversão é Tf = Tc × 1, 8 + 32,
com Tf igual a temperatura em Fahrenheit e Tc igual a temperatura em Celsius.'''

print(           ) #Usado para separar os exercícios na saída.
print('Exercício 2:')

#Teste a)
Tc=-10#∘C
Tf=Tc*1.8+32
print('a.Temperatura=',int(Tf),'°F')

#Teste b)
Tc=30#∘C
Tf=Tc*1.8+32
print('b.Temperatura=',int(Tf),'°F')

#Teste c)
Tc=5#∘C
Tf=Tc*1.8+32
print('c.Temperatura=',int(Tf),'°F')

#------------------------------------------------------------------------------

#Exercício 3: Lado de um triângulo.

'''A resolução desse exercício se baseia na definição da medida de um lado de 
um triângulo, denominado c, a partir os outros lados a e b em conjunto com o 
ângulo θ entre eles, usando a chamada lei dos cossenos: c=a*2+b*2−2*a*b*cos(θ)'''

print(              )
print('Exercício 3:')

#Teste a)
a=1
b=2
θ=30
c=(a*2)+(b*2)-(2*a*b*np.cos(θ))
print("a.Lado c=",round(c,2))

#Teste b)
a=3 
b=1 
θ=45
c=(a*2)+(b*2)-(2*a*b*np.cos(θ))
print("b.Lado c=",round(c,2))

#Teste c)
a=10 
b=11
θ=15
c=(a*2)+(b*2)-(2*a*b*np.cos(θ))
print("c.Lado c=",round(c,2))

#------------------------------------------------------------------------------

#Exercício 4: Série de Fibonacci.

'''Nesse exercício, iremos calcular o i-ésimo número na Série de Fibonacci, 
onde cada número é a soma dos dois números anteriores. Com i representando o 
posicionamento do número na série, temos que:Fi=(((1+√5)/2)**i−((1−√5)/2)**i)/√5'''


print( )
print('Exercício 4:')

#Teste a)
i=30
Fi=(((1+np.sqrt(5))/2)**i-((1-np.sqrt(5))/2)**i)/np.sqrt(5)
print('a.Para i=30,Fi≅',int(Fi))

#Teste b)
i=31
Fi=(((1+np.sqrt(5))/2)**i-((1-np.sqrt(5))/2)**i)/np.sqrt(5)
print('b.Para i=31,Fi≅',int(Fi))

#Teste c)
i=32
Fi=(((1+np.sqrt(5))/2)**i-((1-np.sqrt(5))/2)**i)/np.sqrt(5)
print('c.Para i=32,Fi≅',int(Fi))

#------------------------------ FIM DA TAREFA ---------------------------------












































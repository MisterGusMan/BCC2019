# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 19:07:11 2019

@author: gustavo.fonseca
"""
import numpy as np

#Tarefa 15

'''Esta tarefa involve a criação de uma função que receba um número a, 
um número b e um número x. Esta função deve retornar True se x estiver entre
a e b e False caso contrário. Além disso a função deve mostrar uma mensagem 
dizendo se x está no intervalo entre a e b ou não.'''

def EstaNoIntervalo(a,b,x):
    '''
    Define se um número x esta entre dois números a e b.
    
    Parâmetros:
    -----------------------------
    a e b:
        Números reais que definem o início e o final do intervalo utilizado.
    x:
        Número real que será definido como pertencente ou não no intervalo [a,b]
        
    Retorna
    ----------------------------
   Resposta=boolean:
       Definição se x esta entre a e b (true = sim, false = não).
         
    '''  
    if a < x < b :
        resposta=True
        print(x,'esta entre',a,'e',b)
    else:
        resposta=False
        print(x,' não esta entre',a,'e',b)
        
    return resposta  

a = np.array([-2.5,-10,67.2])
b = np.array([6.3,7,87.2])
x = np.array([9.1,2.2,8.1])
for i in range (3):
    resposta=EstaNoIntervalo(a[i],b[i],x[i])
        
    
               
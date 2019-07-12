# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 19:16:12 2019

@author: gustavo.fonseca
"""
#Tarefa 7
'''Esse script foi criado para a resolução da tarefa 7, no qual estaremos 
definindo se um número inteiro guardado na variável x é par ou ímpar. Para 
definir se o número é par ou ímpar, estaremos usando a função que define o resto
de uma divisão x/y (x%y) para checar se ele é ou não divisível por 2.'''

#Teste a)x=1
x = 1
if x % 2 == 0:#Função que define que o resto da divisão x/2 é 0. Se verdadeira, x é par. Se falsa, x é ímpar.
    print('a)O número',x,'é par.')
else:
    print('a)O número',x,'é ímpar.')
    
#Teste b)x=24
x=24    
if x % 2 == 0:
    print('b)O número',x,'é par.')
else:
    print('b)O número',x,'é ímpar.')
    
#Teste c)x=10  
x=10    
if x % 2 == 0:
    print('c)O número',x,'é par.')
else:
    print('c)O número',x,'é ímpar.')
        
#Teste d)x=5  
x=5    
if x % 2 == 0:
    print('d)O número',x,'é par.')
else:
    print('d)O número',x,'é ímpar.')
            
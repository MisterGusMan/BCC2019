# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:35:44 2019

@author: gustavo.fonseca
"""
import matplotlib.pyplot as plt
import pandas as pd
import funcs as f1

#Tarefa 18

#Exercício 1:
print('Exercício 1')
t=pd.read_csv('file:///C:/Users/gustavo.fonseca/Downloads/BDSinfo.csv', delimiter='\t')
f=t['FootLen']
h=t['Height']
m,b=f1.regressao(h,f)
c1=f1.corr(f,h)
plt.figure()
plt.plot(h,f,marker='o',color='r',linestyle='')
plt.plot(h,(m*h)+b,label='Reta de Regressão')
plt.title('Exercício 1')
plt.ylabel('Tamanho do Pé (FootLen)')
plt.xlabel('Altura (m)')
plt.legend()
plt.grid()
plt.show()

print()

#Exercício 2:
print('Exercício 2')
t=pd.read_csv('file:///C:/Users/gustavo.fonseca/Downloads/inflaAnual.csv')
t1=t[t['Ano']>=1961]
i=t1['Inflação']
t2=pd.read_csv('file:///C:/Users/gustavo.fonseca/Downloads/pibAnual.csv')
p=t2['Variação anual do PIB real (%)']
plt.figure()
plt.plot(p,i,marker='o',color='g',linestyle='')
plt.title('Exercício 2')
plt.ylabel('Inflação anual (%)')
plt.xlabel('Variação do PIB (%)')
plt.grid()
c2=f1.corr(p,i)

print()

#Exercício 3:
print('Exercício 3')
t=pd.read_csv('file:///C:/Users/gustavo.fonseca/Downloads/BDSinfo.csv', delimiter='\t')
n=t['Nmedication']
a=t['Age']
m,b=f1.regressao(a,n)
c1=f1.corr(n,a)
plt.figure()
plt.plot(a,n,marker='o',color='r',linestyle='')
plt.plot(a,(m*a)+b,label='Reta de Regressão')
plt.title('Exercício 3')
plt.ylabel('Número de medicamentos tomados')
plt.xlabel('Idade (Anos)')
plt.legend()
plt.grid()
plt.show()








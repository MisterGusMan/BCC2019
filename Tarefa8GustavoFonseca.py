# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 20:10:40 2019

@author: gustavo.fonseca
"""

'''Esse script será usado para a resolução da tarefa 8. Cada exercício possuirá
comentários explicando como cada parte do script funciona. Algumas soluções 
serão plotadas em gráficos, que serão nomeados para a fácil identificação.'''
import numpy as np
import matplotlib.pyplot as plt


#Exercício 1: Cálculo do IMC.

'''Nesse exercício, estaremos calculando e definindo o índice de massa corporal
(IMC) de uma pessoa, que depende de sua massa(kg) e altura(m). A fórmula usada
é IMC = m/h**2, com m=massa e h=altura. O IMC também pode ser classificado. As
classificações serão definidas com o script abaixo:'''

'''if IMC<17:
    print('Essa pessoa está muito abaixo do peso.')
else:
if 17<=IMC<18.5:
        print('Essa pessoa está abaixo do peso.')
    else: 
        if 18.5<=IMC<25:
            print('Essa pessoa possui peso normal.')
        else:
            if 25<=IMC<30:
                print('Essa pessoa está acima do peso.')
            else:
                if 30<=IMC<35:
                    print('Essa pessoa está com obesidade grau I.')
                else:
                    if 35<=IMC<=40:
                        print('Essa pessoa está com obesidade grau II.')
                    else:
                        if IMC>40:
                          print('Essa pessoa está com obesidade grau III.')''' 

print('Exercício 1:')
#Teste a)                          
m=52
h=1.58        
IMC=m/h**2
print('a)O IMC dessa pessoa é igual a',round(IMC,2),'kg/m**2')#Arrendondaremos o IMC para duas casas decimais.
if IMC<17:
    print('Essa pessoa está muito abaixo do peso.')
else:
    if 17<=IMC<18.5:
        print('Essa pessoa está abaixo do peso.')
    else: 
        if 18.5<=IMC<25:
            print('Essa pessoa possui peso normal.')
        else:
            if 25<=IMC<30:
                print('Essa pessoa está acima do peso.')
            else:
                if 30<=IMC<35:
                    print('Essa pessoa está com obesidade grau I.')
                else:
                    if 35<=IMC<=40:
                        print('Essa pessoa está com obesidade grau II.')
                    else:
                        if IMC>40:
                          print('Essa pessoa está com obesidade grau III.')
                          
print()#Espaço entre respostas.                      
                          
#Teste b)
m=83
h=1.75
IMC=m/h**2
print('b)O IMC dessa pessoa é igual a',round(IMC,2),'kg/m**2')
if IMC<17:
    print('Essa pessoa está muito abaixo do peso.')
else:
    if 17<=IMC<18.5:
        print('Essa pessoa está abaixo do peso.')
    else: 
        if 18.5<=IMC<25:
            print('Essa pessoa possui peso normal.')
        else:
            if 25<=IMC<30:
                print('Essa pessoa está acima do peso.')
            else:
                if 30<=IMC<35:
                    print('Essa pessoa está com obesidade grau I.')
                else:
                    if 35<=IMC<=40:
                        print('Essa pessoa está com obesidade grau II.')
                    else:
                        if IMC>40:
                          print('Essa pessoa está com obesidade grau III.')
     
print()                     
                          
#Teste c)
m=78
h=1.88
IMC=m/h**2
print('c)O IMC dessa pessoa é igual a',round(IMC,2),'kg/m**2')
if IMC<17:
    print('Essa pessoa está muito abaixo do peso.')
else:
    if 17<=IMC<18.5:
        print('Essa pessoa está abaixo do peso.')
    else: 
        if 18.5<=IMC<25:
            print('Essa pessoa possui peso normal.')
        else:
            if 25<=IMC<30:
                print('Essa pessoa está acima do peso.')
            else:
                if 30<=IMC<35:
                    print('Essa pessoa está com obesidade grau I.')
                else:
                    if 35<=IMC<=40:
                        print('Essa pessoa está com obesidade grau II.')
                    else:
                        if IMC>40:
                          print('Essa pessoa está com obesidade grau III.')                          


print()


#Exercício 2: Acidez de uma solução. 
print('Exercício 2:') 
 
'''Nesse exercício, calcularemos a acidez de uma solução de hidróxido de
magnésio em ácido clorídrico. Com "A" sendo a acidez e "x" sendo a concentração 
de íons hidrônio, temos A(x)=(x**3)+3*(x**2)-54.'''

#Teste 1) Gráfico A(x)                     
x=np.arange(0,9)#Concentração entre 0 e 8.                      
A=(x**3)+3*(x**2)-54
y=(x[A==0])
plt.figure()                        
plt.plot(x,A,markevery=y,marker="o",markerfacecolor='red')#O ponto vermelho no gráfico representa a saturação nula da solução.
plt.grid(True)
plt.title('Gráfico exercício 2')
plt.xlabel('Íons hidrônio (Concentração)') 
plt.ylabel('Acidez da solução')                         
plt.show  


#Teste 2) Solução saturada   
print('O valor de x para que a solucão seja saturada é',x[A==0])#Esse comando seleciona a variável x tal que A(x)=0.                   
 
print()

#Exercício 3: Gráfico de uma função.
print('Exercício 3:') 
                       
'''Neste exercício, estaremos plotando o gráfico da função f(x)=|x-2|+|2x+1|-x-6
e definiremos o menor valor de x tal que f(x)>0 e x>0.'''
                        
x=np.arange(-10,11)#X variando de -10 a 10.                          
f=(np.abs(x-2))+(np.abs((2*x)+1))-(x)-(6)#A função "np.abs" é usada para representar o módulo.                       
plt.figure()
plt.plot(x,f,linestyle='--',color='g')
plt.grid(True)
plt.xlabel('X')
plt.ylabel('F(x)')
plt.title('Gráfico exercício 3')
plt.show
print('O menor valor de x tal que x>0 e f(x)>0 é',np.min(x[np.logical_and(x>0,f>0)]))#Valor mínimo de x tal que x>0 e f(x)>0


print()

#Exercício 4:Gráfico de uma função(2).
print('Exercício 4')

'''Assim como no exercício anterior, estaremos plotando o gráfico de uma função.
A função a ser plotada é f(x)=(x**2)-(np.sin(0.784*(x**2)))-2. Também estaremos 
mostrando as raízes de f(x),ou seja, os valores de x tais que f(x)=0.'''
x=np.arange(-10,10,0.0001)#Arranjo de -10 a 10, com incrementos de 0.0001.
f=(x**2)-(np.sin(0.784*(x**2)))-2
plt.figure()
plt.plot(x,f,color='r',linestyle='-.')
plt.grid(True)
plt.title('Gráfico exercício 4')
plt.xlabel('X')
plt.ylabel('F(x)')
plt.show
print('Os valores de x tais que f(x) mais se aproxima de 0 são:',x[np.abs(f)<0.001])

'''Como estamos lidando com números float, não podemos definir as raízes de 
f(x) com exatidão. Entretanto, podemos descobrir valores próximos usando
a função que identifica os valores de x tais que o valor absoluto (módulo) de 
f(x)<1*10**-3.'''




              
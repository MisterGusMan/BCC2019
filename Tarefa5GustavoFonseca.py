#Tarefa 5

'''Esse script foi criado para a resolução da tarefa 5,
que involve a altura de uma bola lançada no ar em 
relação ao tempo. Com o tempo sendo t e
a altura sendo h, temos que h(t)=(-t)**2+(4*t).'''
import matplotlib.pyplot as plt
import numpy as np


#Teste a) Gráfico da altura em função do tempo.

t=np.arange(0, 5, 0.1)#Tempo entre 0 e 5 segundos, com incrementos de 0.1s.
h=-(t)**2+(4*t)
plt.title('Gráfico teste a)')
plt.plot(t,h,color='navy',linestyle='--',)
plt.ylabel('Altura(m)')
plt.xlabel('Tempo(s)')
plt.show


#Teste b) Altura máxima atingida pela bola.

print('b) A altura máxima atingida pela bola é',np.max(h),'metros.')
#Usamos o comando "np.max(h)" para definir o valor máximo da função h.

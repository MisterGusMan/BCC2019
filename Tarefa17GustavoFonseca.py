# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 18:58:05 2019

@author: gustavo.fonseca
"""

import pandas as pd
import funcs as f1


#Tarefa 17

#Função utilizada no arquivo 'funcs.py'

#Teste com as colunas 'Renda (R$)' e 'Público' da tabela do Campeonato Brasileiro.
    
t=pd.read_csv('file:///C:/Users/gustavo.fonseca/Downloads/tabelaBrasileirao2018.csv')  
x1=t['Público'] 
y1=t['Renda (R$)']
r1=f1.corr(x1,y1)
        
        


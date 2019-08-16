import numpy as np

def regressao(x, y):
    '''
    Calcula a inclinação m ep intercepto b da reta de regressão utilizado o método dos 
    mínimos quadrados. 
    
    Parâmetros:
    -------------------------------
    x: vetor
       vetor contendo os valores do vetor x
    
    y: vetor
       vetor contendo os valores do vetor y
       
    Retorna
    -------------------------------
    
    m: float
       inclinação da reta de regressão
       
    b: float
       intercepto da reta de regressão
    '''
    m = mediaX = np.mean(x)
    mediaY = np.mean(y)
    desvioX = x - mediaX
    desvioY = y - mediaY
    m = np.sum(desvioX*desvioY)/np.sum(desvioX**2)
    b = mediaY - m*mediaX
    
    return m, b

def corr(x,y):
    '''
    Define a correlação r entre dois vetores ou colunas de uma DataFrame do Pandas.
    
    Parâmetros:
    ---------------------------------------------------------------------------    
        x e y: vetores contendo os diferentes valores dos dois vetores escolhidos.
        
    Retorna:
    --------------------------------------------------------------------------- 
        r: valor inteiro contido no intervalo [-1;1], representando a correlação
        entre os dois vetores escolhidos (correlação linear negativa, positiva ou nula).
    '''
    mx = np.mean(x)
    my = np.mean(y)
    dx = x - mx
    dy = y - my
    r=np.sum(dx*dy)/(np.sqrt(np.sum(dx**2))*np.sqrt(np.sum(dy**2)))
    print('A correlação entre os vetores é',r)
    return r

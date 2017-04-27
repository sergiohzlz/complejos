#!/usr/bin/python
#-*-coding:utf8-*-

import numpy as np

def crea_matriz(dimension, S=[1,2], p=0.9):
    """
    Crea una matriz de las dimensiones especificadas en el parámetro
    a una densidad especificada por el parámetro p con los simbolos
    en el parámetro S
    Regrsa tres objetos
    Z: La matriz ocupada
    V: Las entradas de la matriz vacias
    O: Las entradas de la matriz ocupadas
    """
    M, N = dimension
    Z = np.zeros(dimension, dtype=int)
    V, O = [], []
    for i in range(M):
        for j in range(N):
            v = np.random.rand()
            if(v<=p):
                k = np.random.choice(S)
                Z[i,j] = k
                O.append((i,j))
            else:
                V.append((i,j))
    return Z,V,O

def vecindad(coord,M):
    """
    Recupera la vecindad de Moore de la coordenada coord
    en el parámetro en la matriz M y regresa las coordenadas
    en una lista
    Ej:
    vecindad((5,5))
    [(4,4),(5,4),(6,4),(4,5),(6,5),(6,4),(6,5),(6,6)]
    """
    m,n = M.shape
    x,y = coord
    V = [(i,j) for i in (-1,0,1) for j in (-1,0,1)]
    V.remove((0,0))
    P = [((x+c[0])%m, (y+c[1])%n) for c in V]
    C = []
    for p in P:
        C.append( M[p] )
    return C

def n_vecinos(V,M,S=[1,2]):
    """
    Determina la proporción de cada tipo de vecino en la vecindad
    V en la matriz M. Los diferentes tipos se especifican en el
    parámetro S.
    Regresa una lista  diccionario que contiene la cantidad de cada
    tipo de vecino en V.
    Ejemplo. Considerando que M es una matriz de 3x3 como sigue:
    M =array([[1, 1, 1],
              [2, 2, 2],
              [0, 1, 2]])

    Si recuperamos la vecindad de la coordenada (2,2)

    V = vecindad((2,2),M)

    el diccionario que deberíamos obtener con el conteo de
    los diferentes vecinos es:

    {0:1 1: 4, 2: 3}
    """
    D = dict()
    for vecino in V:
        #vecino = M[coord]
        D[vecino] = D.get(vecino,0) + 1
    return D

def umbral(V,c,ro, M):
    """
    Determina si el vecino en la celda c
    rebasa el umbral ro en la vecindad V
    todo en la malla M
    """
    t = M[c]
    D = n_vecinos(V,M)
    nv = D[t]
    tv = D[1] + D[2] #total de vecinos 1 y 2
    u = 1.*nv/tv
    if u>=ro:
        return True
    elif u<ro:
        return False



if __name__=='__main__':
    umbral = float(sys.argv[1])

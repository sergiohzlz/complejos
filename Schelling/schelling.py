#!/usr/bin/python
#-*-coding:utf8-*-

import numpy as np
import sys

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

def n_vecinos(V,M,S=[0,1,2]):
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
    for v in S:
        D[v] = 0
    for vecino in V:
        #vecino = M[coord]
        D[vecino] += 1
    return D

def umbral(V,c,ro, M, dbg=False):
    """
    Determina si el vecino en la celda c
    rebasa el umbral ro en la vecindad V
    todo en la malla M.
    Si el vecino en la celda c rebasa
    el umbral, regresa True, en caso
    contrario regresa False.
    """
    t = M[c]
    if dbg: print("El vecino: M[{0}] es de tipo {1}".format(c,t))
    D = n_vecinos(V,M)
    nv = D.get(t,0)
    tv = D.get(1,0) + D.get(2,0) #total de vecinos 1 y 2
    u = 1.*nv/tv
    if u>=ro:
        return True
    elif u<ro:
        return False

def reubica(c,V,O,M, dbg = False):
    """
    Reubica al vecino M[c] a una de
    las celdas v en V
    """
    jn = np.random.choice(range(len(V)))
    n = V[jn]
    if dbg: print("Coordenada vacía: V[{0}]={1} ".format(jn,n))
    t = M[c]
    M[n] = t
    M[c] = 0
    O.remove(c)
    V.append(n)
    np.random.shuffle(V)
    np.random.shuffle(O)
    return n

def obten_inconformes(M,th):
    m, n = M.shape
    I = []
    for i in range(m):
        for j in range(n):
            c = (i,j)
            V = vecindad(c,M)
            u = umbral(V,c,th,M)
            if not u: I.append( (i,j) )
    return I

if __name__=='__main__':
    thrsl  = float(sys.argv[1])
    dimen  = tuple(map(int, sys.argv[2].split(",")))
    M,V,O  = crea_matriz(dimen)
    m,n    = M.shape
    #primero escaneamos los vecinos que no estén
    #contentos
    I = obten_inconformes(M,thrsl)
    np.random.shuffle(I)
    print("Originales: {0}".format(len(I)))
    # comenzamos el algoritmo
    while(len(I)>0):
        o = I.pop()
        U = vecindad( o, M )
        u = umbral(U, o, thrsl, M)
        if(not u):
            k = reubica(o,V,O,M)
            U = vecindad( k, M )
            u = umbral( U, k, thrsl, M )
            if(not u):
                I.append(k)
        print("{0}".format(len(I)))

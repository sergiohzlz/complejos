#!/usr/bin/python
#-*-coding:utf8-*-

import numpy as np
import sys

def crea_matriz(dimension, S=[1,2], p=0.9, dbg=False):
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
    if(dbg):
        print(Z)
        print(map(str,V))
        print(map(str,O))
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
    #rellenamos valores por defecto
    for v in S:
        D[v] = 0
    #contamos los vecinos y los guardamos
    # en el diccionario
    for vecino in V:
        D[vecino] += 1
    return D

def umbral(V,c,th, M, dbg=False):
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
    nv = D[t]        #numero de vecinos de mi tipo
    tv = D[1] + D[2] #total de vecinos 1 y 2
    if(tv>0):
        p = 1.*nv/tv     #proporcion de vecinos en la vecindad
        if p>=th:
            return True
        elif p<th:
            return False
    elif(tv==0):
        return True

def reubica(c,V,O,M, dbg = False):
    """
    Reubica al vecino M[c] a una de
    las celdas v en V
    """
    if dbg:
        print("Reubica")
        print("c:{0}".format(",".join(map(str,c))))
        print("V:{0}".format(",".join(map(str,V))))
        print("O:{0}".format(",".join(map(str,O))))
    #jn = np.random.choice(range(len(V)))
    np.random.shuffle(V)
    n = V.pop()
    if dbg: print("Coordenada vacía: V[{0}]={1} ".format(n,V[n]))
    t = M[c]
    M[n] = t
    O.append(n)
    M[c] = 0
    V.append(c)
    O.remove(c)
    np.random.shuffle(V)
    np.random.shuffle(O)
    return n

def obten_inconformes(M,th,O):
    m, n = M.shape
    I = []
    for c in O:
        t = M[c]
        V = vecindad(c,M)
        u = umbral(V,c,th,M)
        if(not u): I.append(c)
    return I

if __name__=='__main__':
    thrsl  = float(sys.argv[1])
    dimen  = tuple(map(int, sys.argv[2].split(",")))
    ro     = float(sys.argv[3])
    M,V,O  = crea_matriz(dimen, p=ro)
    print(M)
    m,n    = M.shape
    #primero escaneamos los vecinos que no estén
    #contentos
    I = obten_inconformes(M,thrsl,O)
    np.random.shuffle(I)
    #print(len(I))
    # comenzamos el algoritmo
    while(len(I)>0):
        o = I.pop()
        W = vecindad( o, M )
        u = umbral(W, o, thrsl, M)
        if(not u):
            k = reubica(o,V,O,M)
            U = vecindad( k, M )
            u = umbral( U, k, thrsl, M )
            if(not u):
                I.append(k)
        #print("{0}".format(len(I)))
    print(M)

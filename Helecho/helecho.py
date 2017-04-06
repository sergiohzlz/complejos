#!/usr/bin/python2.7
import random
import sys
from pylab import array, dot


def helecho(C,P,K=10000):
    """
    Funcion helecho.
    Calcula un conjunto de puntos iterando K veces
    las funciones de la forma

    f(x,y) = Mx + B

    donde M es una matriz cuadrada, y x,B son vectores
    columna

    El parametro C es una lista de lista, donde cada elemento
    contiene las diferentes entradas de la matriz M y B. Los
    primeros 4 corresponden a las entradas de M y los ultimos
    dos a B.

    El parametro P=[p1,p2,p3,p4] es el conjunto de probabilidades
    con las que cada ecuacion es elegida de tal forma que

    [0,p1) U [p1,p2) U [p2,p3) U [p3,p4] = [0,1]
    """
    x0, y0 = 0.5, 0.
    X = [x0]
    Y = [y0]
    p1,p2,p3,p4 = P
    C0,C1,C2,C3 = C
    for i in range(K):
        x = X[-1]
        y = Y[-1]
        Pa = array([[x],[y]])
        rand = (random.uniform(0,1))
        if (rand < p1):
            a,b,c,d,e,f = C0
        elif  ((p1 <= rand) and (rand <= p2)):
            a,b,c,d,e,f = C1
        elif  ((p2 < rand) and (rand <= p3)):
            a,b,c,d,e,f = C2
        elif ((p3 < rand) and (rand <= p4)):
            a,b,c,d,e,f = C3
        M = array([[a,b],[c,d]])
        B = array([[e],[f]])
        Pn = dot(M, Pa)
        Pn = Pn + B
        x = Pn[0][0]
        y = Pn[1][0]
        X.append(x)
        Y.append(y)
    return array(X),array(Y)

if __name__ == '__main__':
    iters = int(sys.argv[1])
    #params = map(float, sys.argv[2].split(","))
    paramshelecho = sys.argv[2]
    f = open(paramshelecho, "r")
    C = []
    params = []
    for l in f:
        C.append( [float(x) for x in l.strip().split(",")] )
        params.append(C[-1].pop())
    f.close()
    X,Y = helecho(C,params,iters)
    for x,y in zip(X,Y):
        print x,"\t",y

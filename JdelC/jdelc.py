#!/usr/bin/python

import numpy as np
import numpy.random as rnd
import sys
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from numpy import pi

poligono_p    = lambda n,rot: [(1,i*2*np.pi/n+rot) for i in range(1,n+1)]
pol2cart      = lambda ro,te: (ro*np.cos(te),ro*np.sin(te))
poligono_c    = lambda L: [pol2cart(x[0],x[1]) for x in L]
genera_coords = lambda L,p: dict(zip(L,p))
pmedio        = lambda x,y: (0.5*(x[0]+y[0]) , 0.5*(x[1]+y[1]) )

class JdelC(object):
    def __init__(self):
        pass

def juego(n,m=100000, rot=pi/2):
    C = genera_coords(range(n), poligono_c(poligono_p(n,rot)))
    P = [C[rnd.choice(range(n))]]
    for i in range(m):
        up = P[-1]
        vz = C[rnd.choice(range(n))]
        P.append(pmedio(up,vz))
    return np.array(P), C

def juego_sec(V,S,m=100000,rot=pi/4):
    n = len(V)
    C = genera_coords(V, poligono_c(poligono_p(n,rot)))
    P = [C[S[0]]]
    cont = 0
    for i in range(1,m):
        up = P[-1]
        vz = C[S[i]]
        P.append(pmedio(up,vz))
    return np.array(P), C

def secciones_nucleotidos(f,m):
    cont=0
    for r in f:
        l = r.strip()
        if(l[0]=='>'):
            continue
        acum = m-cont
        sec = ''.join([ s for s in l[:acum] if s!='N' ])
        cont+=len(sec)
        if(cont<=m):
            yield sec

def secciones(f,m):
    cont=0
    for r in f:
        l = r.strip()
        try:
            if(l[0]=='>'):
                continue
        except:
            continue
        acum = m-cont
        sec = ''.join([ s for s in l[:acum] ])
        cont+=len(sec)
        if(cont<=m):
            yield sec


def grafica(R):
    plt.scatter(R[:,0],R[:,1],s=0.1, c='k')

def grafcoords(*D):
    R,C = D
    plt.scatter(R[:,0],R[:,1],s=0.1, c='k')
    for c in C:
        plt.annotate(c,C[c])


if __name__=='__main__':
    n = int(sys.argv[0])
# Ejemplo
# In [150]: G = open('Saccharomyces_cerevisiae_aa.fasta','r')
#
# In [151]: secs = jdelc.secciones(G,1000)
#
# In [152]: secuencia = ''
#
# In [153]: for sec in secs:
#      ...:     secuencia += sec
#      ...:
#
# In [154]: R,C = jdelc.juego_sec(aminos,secuencia, len(secuencia),pi/4); jdelc.grafcoords(R,C); show()

#!/usr/bin/python

import numpy as np
import numpy.random as rnd
import sys
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

poligono_p    = lambda n,rot: [(1,i*2*np.pi/n+rot) for i in range(1,n+1)]
pol2cart      = lambda ro,te: (ro*np.cos(te),ro*np.sin(te))
poligono_c    = lambda L: [pol2cart(x[0],x[1]) for x in L]
genera_coords = lambda L,p: dict(zip(L,p))
pmedio        = lambda x,y: (0.5*(x[0]+y[0]) , 0.5*(x[1]+y[1]) )
rot           = np.pi/2

class JdelC(object):
    def __init__(self):
        pass


def juego(n,m=100000):
    C = genera_coords(range(n), poligono_c(poligono_p(n,rot)))
    P = [C[rnd.choice(range(n))]]
    for i in range(m):
        up = P[-1]
        vz = C[rnd.choice(range(n))]
        P.append(pmedio(up,vz))
    return np.array(P)

def juego_sec(V,S,m=100000,rot=np.pi/4):
    n = len(V)
    C = genera_coords(V, poligono_c(poligono_p(n,rot)))
    P = [C[S[0]]]
    cont = 0
    for i in range(1,m):
        up = P[-1]
        vz = C[S[i]]
        P.append(pmedio(up,vz))
    return np.array(P), C

def secciones(G,m):
    cont=0
    while(cont<m):
        for l in G:
            sec = ''.join([s for s in l if s!='N'])
            cont += len(sec)
            yield sec

def lector_fasta(fnom, m=100000):
    G,acum = [],0
    with open(fnom,'r') as f:
        for r in f:
            if(r!='>'):
                lv = r.strip()
                acum += len(lv)



def grafica(R):
    plt.scatter(R[:,0],R[:,1],s=0.1, c='k')

if __name__=='__main__':
    n = int(sys.argv[0])


#!/usr/bin/python

import numpy as np
import numpy.random as rnd
import sys
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

poligono_p    = lambda n: [(1,i*2*np.pi/n+np.pi/2) for i in range(1,n+1)]
pol2cart      = lambda ro,te: (ro*np.cos(te),ro*np.sin(te))
poligono_c    = lambda L: [pol2cart(x[0],x[1]) for x in L]
genera_coords = lambda L,p: dict(zip(L,p))
pmedio        = lambda x,y: (0.5*(x[0]+y[0]) , 0.5*(x[1]+y[1]) )

def juego(n,m=100000):
    C = genera_coords(range(n), poligono_c(poligono_p(n)))
    P = [C[rnd.choice(range(n))]]
    for i in range(m):
        up = P[-1]
        vz = C[rnd.choice(range(n))]
        P.append(pmedio(up,vz))
    return np.array(P)

def grafica(R):
    plt.scatter(R[:,0],R[:,1],s=0.1, c='k')

if __name__=='__main__':
    n = int(sys.argv[0])


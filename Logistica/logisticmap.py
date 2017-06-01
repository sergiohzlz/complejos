#!/usr/bin/python
#-*-coding:utf8-*-

import sys
from pylab import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
plt.style.use('ggplot')

def logistica(x0,r, n=1000):
    L = [x0]
    for i in range(n):
        x_act = L[-1]
        L.append(r*x_act*(1-x_act))
    return L

def bifurcaciones(x0,rango,step,n,k):
    print("x0 ",x0)
    print("rango ",rango[0]," - ",rango[1])
    R = arange(rango[0],rango[1],step)
    m =(rango[1]-rango[0])/step
    m *= (n-k)
    m += (n-k)
    S = zeros((int(m),2))
    print(S.shape)
    i,j=0,0
    for r in R:
        #print "r {0}".format(r)
        L = logistica(x0,r,n)
        for p in L[k+1:]:
            S[i]=(r,p)
            i += 1
    return S

if __name__=='__main__':
    figura = sys.argv[1]
    inicio = float(sys.argv[2])
    fin = float(sys.argv[3])
    x0 = float(sys.argv[4])
    rango = [inicio, fin]
    iters = 500
    #x0 = 0.2
    S = bifurcaciones(x0, rango,0.001,iters,200)
    fig = figure()
    title('Bifurcaciones para el rango '+str(rango))
    xlim(tuple(rango))
    scatter(S[:,0],S[:,1], s=0.01, c='blue')
    savefig(figura+'.png')

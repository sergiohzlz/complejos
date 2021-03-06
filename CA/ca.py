#!/usr/bin/python2
#coding:utf8

import sys
from random import choice
from numpy import array, dot, zeros, hstack, ndarray
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt


class ECA(object):
    def __init__(self, regla, its, longitud, ci='random'):
        self.iters = its
        self.R     = list(reversed(('0'*8 + bin(regla)[2:])[-8:]))
        self.L     = longitud
        self.M     = zeros((its, longitud),dtype='int')
        if(ci=='random'):
            ci = array([choice([0,1]) for i in range(longitud)])
        elif (type(ci)==list) or (type(ci)==ndarray):
            self.ci = ci
        self.M[0] = ci
    def salva(self, fname, titulo=''):
        fig,ax = plt.subplots()
        ax.imshow(self.M)
        ax.set_title(titulo)
        fig.savefig(fname)
        del(fig)
        del(ax)
    def ejecuta(self):
        for i in range(1,self.iters):
            self.M[i] = self.itera(self.M[i-1])
    def itera(self, ant):
        r = self.R
        L = self.L
        S = []
        for j in range(len(ant)):
            vec = str(ant[(j-1)%L]) + str(ant[j]) + str(ant[(j+1)%L])
            s = r[int( vec,2 )]
            S.append(s)
        return S
    def simulacion(self):
        return self.M



if __name__=='__main__':
    regla = int(sys.argv[1])
    iters = int(sys.argv[2])
    lngtd = int(sys.argv[3])
    salida = sys.argv[4]

    ca = ECA(regla, iters, lngtd)
    ca.ejecuta()
    ca.salva(salida)

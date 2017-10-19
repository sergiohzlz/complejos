#!/usr/bin/python2
#coding:utf8

import sys
from random import choice
from numpy import array, dot, zeros, hstack
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt


class ECA(object):
    """
    Clase para implementar un autómata celular unidimensional
    """
    def __init__(self, regla, its, longitud, ci='random'):
        """
        Constructor. Recibe la regla en decimal, número de
        iteraciones y la longitud del arreglo.
        ci puede ser 'random' o un vector especificando la
        condición inicial.
        Una vez especificado hay que ejecutar la función
        'ejecuta' para que se lleve a cabo el cómputo.
        """
        self.iters = its
        self.R     = ('0'*8 + bin(regla)[2:])[-8:]
        self.L     = longitud
        self.M     = zeros((its, longitud))
        if(ci=='random'):
            ci = array([choice([0,1]) for i in range(longitud)])
        elif (type(ci)==list) or (type(ci)==numpy.ndarray):
            self.ci = ci
        self.M[0] = ci
    def salva(self, fname, titulo=''):
        """
        Salva la imagen en png con el nombre
        fname
        """
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
            vec = hstack( (ant[(j-1)%L] , ant[j%L], ant[(j+1)%L]) ).astype(int)
            s = r[7-int(''.join(map(str, vec)),2)]
            S.append(s)
        return S
    def simulacion(self):
        """
        Regrsa la simulación
        """
        return self.M



if __name__=='__main__':
    regla = int(sys.argv[1])
    iters = int(sys.argv[2])
    lngtd = int(sys.argv[3])
    salida = sys.argv[4]

    ca = ECA(regla, iters, lngtd, iters)
    ca.ejecuta()
    ca.salva(salida)

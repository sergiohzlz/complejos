#!/usr/bin/python2.7
#-*- coding:utf-8 -*-

import sys                        #importamos la biblioteca sys

def logistica(x0, r, n=1000):  #observen que estoy inicializando n con un valor de 1000 por defecto
    """
    Calcula los estados de la función logística
    x_t+1= x_t * r * (1 - x_t)
    Usando los parametros
    x0: punto inicial, flotante
    r:  constante de carga, flotante
    n:  duración, entero
    
    Regresa
    Una lista con toda la evolución
    """
    L = [x0]
    for i in range(n):
        xact = L[-1]           #punto actual
        xsig = xact*r*(1-xact) #punto siguiente
        L.append(xsig)         #lo ponemos en la lista para que sea tomado en la siguiente iteración
    return L
    
def mapeo(parametros):
    """
    Función mapeo. Esta función la deben implementar
    y debe recibir algunos parámetros que ustedes deben
    determinar para luego llamar a la función logística, recibir
    las iteraciones, desechar el transitorio y luego quedarse 
    con los puntos restantes, todo esto para cada valor de r
    que deberán ir variando entre 2 y 4
    """
    pass
    
if __name__=='__main__':
    x0 = float(sys.argv[1]) #leemos el parámetro x0
    r  = float(sys.argv[2]) #leemos el parámetro r
    n  = int(sys.argv[3])   #leemos las iteraciones
    
    iteraciones = logistica(x0, r, n)
    for val in iteraciones:
        print val

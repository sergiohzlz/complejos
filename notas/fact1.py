#!/usr/local/bin/python
#-*- coding:utf8 -*-
import sys

def factorial(n):
    r = 1
    for i in range(1,n+1):
        r *= i
    return r

if __name__ == '__main__':
    num = int(sys.argv[1])
    fact = factorial(num)
    print("Factorial de {0} es {1}".format(num,fact))


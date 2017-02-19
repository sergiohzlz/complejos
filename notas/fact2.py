#!/usr/local/bin/python
#-*- coding:utf8 -*-
import sys

def factorial(n):
    R = [1]
    for i in range(1,n+1):
        r = R[-1]*i
        R.append(r)
    return R[-1]

if __name__ == '__main__':
    num = int(sys.argv[1])
    fact = factorial(num)
    print("Factorial de {0} es {1}".format(num,fact))


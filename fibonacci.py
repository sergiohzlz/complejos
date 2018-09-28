#!/usr/bin/python
#coding:utf8

def fib_lista(n):
    L = [0,1]
    for i in range(2,n+1):
        L.append(L[i-1] + L[i-2])
    return L[-1]

def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        m = fibonacci(n-1) + fibonacci(n-2)
        print(m)
        return m




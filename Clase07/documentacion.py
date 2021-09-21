#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 00:07:27 2021

@author: cris
"""
#%%
def valor_absoluto(n):
    ''' Recibe un número y devuelve su valor absoluto'''
    if n >= 0:
        return n
    else:
        return -n

#%%    
def suma_pares(l):
    ''' Recibe una lista de números y devuelve la suma de 
    los números pares que la componen'''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res

# Pre = l es una lista de números
# Pos = devuelve el resultado de la suma de los números pares 
# Invariante = res es el resultado de la suma 

#%%
def veces(a, b):
    '''Recibe dos números a y b, y devuelve el resultado de sumar b 
    veces el numero a'''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res

# Pre = b >= 0
# Pos = a * b
# Invariante = res

#%%
def collatz(n):
    '''Recibe un número >= 1. Devuelve la cantidad de ciclos que se realizaron.
    '''
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res

# Pre = n >= 1
# Pos = 
# Invariante = res 


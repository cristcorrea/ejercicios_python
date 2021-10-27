#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 19:11:51 2021

@author: cris
"""

def bbinaria_rec(lista, e):
    '''Busca un elemento e en lista''' 
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if lista[medio] == e:
            res = True
        elif lista[medio] < e:
            res = bbinaria_rec(lista[medio:], e)
        else:
            res = bbinaria_rec(lista[:medio], e)
    return res


lista1 = [1,2,3,5,6,7,8,9]
prueba = bbinaria_rec(lista1, 2)
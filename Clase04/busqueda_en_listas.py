#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 08:26:52 2021

@author: cris
"""

def buscar_u_elemento(lista, u):
    pos = -1
    for i, j in enumerate(lista): 
        if j == u:
            pos = i
    return pos

def buscar_n_elemento(lista, n):
    veces = 0
    for i, j in enumerate(lista):
        if j == n:
            veces += 1
    return veces

def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = lista[0] # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e
    return m
    
def busqueda_lineal_ordenada(lista, e):
    pos = -1
    lista.sort()
    for i, z in enumerate(lista):
        if z == e:
            pos = i
            break
        elif z >= e:
            break
    return pos

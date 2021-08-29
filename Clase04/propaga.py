#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 11:36:43 2021

@author: cris
"""

def propagar(lista):
    L = lista
    for i, j in enumerate(lista):
        tamanio = len(lista)-1
        n = i
        if j == -1:
            L[i] = j
        elif j == 0:
            L[i] = j
        elif j == 1:
            while n != 0:
                if lista[n-1] == 0:
                    L[n-1] = 1
                    n -=1
                else:
                    n = 0
            n = i
            while n < tamanio:
                if lista[n+1] == 0:
                    L[n+1] = 1
                    n += 1
                else:
                    n = tamanio
    return L
            
                
            
        
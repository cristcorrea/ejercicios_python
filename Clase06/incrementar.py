#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 17:09:36 2021

@author: cris
"""

def incrementar(s):
    carry = 1
    l = len(s)

    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    print(s)
    return s

def listar_secuencias(n):
    secuencia = [0]*n
    print(secuencia)
    for i in range(2**n-1):
        secuencia = incrementar(secuencia)
        
    
''' Respondiendo a la pregunta 6.18 la función listar_secuencias es de
tipo exponencial ya que la cantidad de secuencias crece 2 a la n veces'''

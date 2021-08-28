#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 21:18:16 2021

@author: cris
"""

def invertir_lista(lista):
    invertida = []
    i = -1
    for e in lista: # Recorro la lista
        invertida.append(lista[i])
        i -= 1
    return invertida
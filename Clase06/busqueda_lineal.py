#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 14:03:11 2021

@author: cris
"""
# def busqueda_lineal(lista, e):
#     '''Si e está en la lista devuelve su posición, de lo
#     contrario devuelve -1.
#     '''
#     pos = -1  # comenzamos suponiendo que e no está
    
#     for i, z in enumerate(lista): # recorremos la lista
#         if z == e:   # si encontramos a e
#             pos = i  # guardamos su posición
#             break    # y salimos del ciclo
#     return pos

def busqueda_lineal(lista, e):
    pos = -1
    lista.sort()
    for i, z in enumerate(lista):
        if z == e:
            pos = i
            break
        elif z >= e:
            break
    return pos
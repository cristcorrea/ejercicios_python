#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 17:52:19 2021

@author: cris
"""

numeros = [0,1,2,3,4,5,6,7,8,9]
lista2 = []
for i, numero in enumerate(numeros):
    valor = numero
    resultado = 0
    lista = [0]
    for numero in range(9):
        resultado += int(valor)
        lista.append(resultado)
    lista2.append(tuple(lista))

print("{:>5}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}".format("0","1", "2","3", "4", "5", "6", "7", "8", "9"))
print("-------------------------------")
for i, tupla in enumerate(lista2):
    print("{:d}{:>1s}{:>3d}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3d}".format(i,":",tupla[0], tupla[1], tupla[2], tupla[3], tupla[4], tupla[5],
                                              tupla[6],tupla[7],tupla[8],tupla[9]))

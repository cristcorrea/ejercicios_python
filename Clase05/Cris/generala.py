#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 23:49:50 2021

@author: cris
"""
import random
from collections import Counter

def tirar():
    tirada=[]
    for i in range(5):
        tirada.append(random.randint(1,6)) 
    print(tirada)
    return tirada



def es_generala(tirada):
    tamanio = len(tirada)-1
    i = 0
    salida = False
    repetido = 0
    while i < tamanio:
        if tirada[i] == tirada[i+1]:
            i += 1
            if i == 4:
                salida = True
        else: i += 1
    if salida == False:       
        lista = ([(x,y) for x, y in Counter(tirada).items() if y > 1])
        maximo = max([y for x,y in Counter(tirada).items()])
        for x,y in lista:
            if y == maximo:
                repetido = x
    return repetido

prueba = es_generala([6,5,5,1,1])
print(prueba)
# N = 1000000
# G = sum([es_generala(tirar()) for i in range(N)])
# prob = G/N
# print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
# print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
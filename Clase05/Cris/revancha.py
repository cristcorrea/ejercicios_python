#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 19:52:04 2021

@author: cris
"""

''' Hasta aca la función chequea si hay generala y, si no la hay,
obtiene el número que mas veces se repite'''

import random
from collections import Counter

def tirar():
    tirada=[]
    for i in range(5):
        tirada.append(random.randint(1,6)) 
    return tirada

"""
La funcion es_generala() toma la lista generada por tirar() y chequea si se obtuvo generala. 
Si hay generala, la  variable salida pasa a True, sino obtiene el valor mas repetido y vuelve a 
arrojar aquellos dados de valores distintos. Todo el ciclo lo realiza 3 veces. """

def es_generala(tirada):
    salida = False
    repetido = 0
    tiro = 0
    for tiro in range(3): # Hace 3 tiros 
        if tirada[0] == tirada[1] == tirada[2] == tirada[3] == tirada[4]: # Chequeo si es generala
            salida = True
        elif salida == False:       # No es generala => 
            lista = ([(x,y) for x, y in Counter(tirada).items() if y > 1]) # Cuento repeticiones 
            maximo = max([y for x,y in Counter(tirada).items()]) # Obtengo la max cantidad de repeticiones
            for x,y in lista: 
                if y == maximo:
                    repetido = x # Devuelvo el numero que mas se repite
            for j, numero in enumerate(tirada): # Vuelvo a tirar los dados no repetidos
                if numero != repetido:
                    tirada[j] = (random.randint(1,6))
            if tirada[0] == tirada[1] == tirada[2] == tirada[3] == tirada[4]: # Vuelvo a chequear si es generala
                salida = True
        tiro += 1
    return salida # Devuelve True si en alguno de los 3 tiros hubo generala


N = 10000
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')


    

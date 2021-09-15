#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 12:25:45 2021

@author: cris
"""
from collections import Counter
import random

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]
reparto = random.sample(naipes,k=3)

limpieza = [reparto[i][1] for i,naipe in enumerate(reparto)] # Obtiene los palos de las barajas recibidas 
envido = dict(Counter(limpieza)) # Cuenta las barajas de cada palo

lista_envido = []
for key, value in envido.items():
    if value >= 2:
        print(f'Hay envido de {key}: {reparto}')

def sumar_envido(reparto):
    for carta in dict(reparto):
        print(carta)
    
    



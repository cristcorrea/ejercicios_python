#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 23:32:49 2021

@author: cris
"""

import random
from collections import Counter


def tirar2(n):
    '''Recibe un número natural n, arroja n veces un dado y devuelve 
    una tupla con el número mas repetido y la cantidad de veces'''
    tirada = []
    for i in range(n):
        tirada.append(random.randint(1,6)) #Tiro los dados
    contador=Counter(tirada).most_common(1)
    mas_comun = tuple((contador[0][0], contador[0][1]))             #valor que mas se repitio              #cantidad de veces que salio el valor
    return mas_comun

def armar_generala(n):
    repetidos = tirar2(n)
    tirada = []
    [tirada.append(repetidos[0]) for valor in range(repetidos[1])]
    return tirada, repetidos

def es_Generala2():
    tiros = 3
    dados = 5
    if tiros == 0:
        jugada = tirar2(dados)
        armar_generala(jugada)
        
    


prueba = armar_generala(5)
print(prueba)

def tirar():
    tirada=[]                   #tirada final
    tirada1=[]
    tirada2=[]
    tirada3=[]
    elegido=0
    veces=0
    for i in range(5):
        tirada1.append(random.randint(1,6)) #Tiro los dados
    n=Counter(tirada1).most_common(1)
    elegido=n[0][0]             #valor que mas se repitio
    veces=n[0][1]               #cantidad de veces que salio el valor

    for j in range(veces):
        tirada.append(elegido)  #agrego el valor en la tirada general
    
    for p in range(5-veces):
        tirada2.append(random.randint(1,6)) #Tiro los dados que me sobraron
    for f in tirada2:
        if f==elegido:
            tirada.append(f)
            veces=veces+1
    
    for g in range(5-veces):
        tirada3.append(random.randint(1,6)) #Tiro los dados que me sobraron
    for h in tirada3:
        tirada.append(h)
        veces=veces+1
    return tirada


def es_generala (tirada):
    if(all(x==tirada[0] for x in tirada)):  #Si todos los valores son iguales
        return True
    else:
        return False  


def  prob_generala(N):
    G = sum([es_generala(tirar()) for i in range(N)])
    prob = G/N
    return prob


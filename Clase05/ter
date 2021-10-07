#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 23:17:48 2021

@author: cris
"""
#%%
import random

mu = 37


def medir_temp(n):
    medicion = [round(random.normalvariate(37,0.2), 2) for valor in range(n)]
    return medicion 

def resumen_temp(n):
    '''máximo, el mínimo, el promedio y la mediana (en ese orden)'''
    medicion = medir_temp(n)
    maximo = max(medicion)
    minimo = min(medicion)
    promedio = round(sum(medicion)/n , 2)
    mitad = len(medicion)/2 
    
    if (mitad % 2) == 0:
        mediana = (medicion[int(mitad)] + medicion[int(mitad+1)])/2
    else:
        mediana = medicion[int(mitad)]
    resultado = (maximo, minimo, promedio, mediana)
    return resultado
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 16:15:39 2021

@author: cris
"""

def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    if hasta < desde:
        return 0
    i = desde
    rango = hasta-desde
    while i < rango:
        desde += desde+1
        i += 1
    return desde



def sumar_enteros2(desde, hasta):
    x = hasta*(hasta+1)/2
    return x

resultado = int(sumar_enteros(1, 5))
print(resultado)
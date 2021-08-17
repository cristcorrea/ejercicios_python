#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 19:17:01 2021

@author: cris
"""
def dicc_geringoso(lista): 
    diccionario = {}
    for palabra in lista: 
        cadena = ''
        for c in palabra: 
            if c in 'aeiouAEIOU': 
                cadena += c + 'p'
            cadena += c
        diccionario[palabra] = cadena
    print(diccionario)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 19:49:41 2021

@author: cris
"""

def precio_fruta(fruta): 
    f = open("Data/precios.csv", "rt")
    resultado = ""
    for line in f: 
        row = line.split(",")
        if fruta in row:
            resultado = "El precio de un cajón de {} es $ {}".format(fruta,str.rstrip(row[-1]))
            break
        else:
            resultado = "{} no figura en la lista de precios".format(fruta)
    return resultado
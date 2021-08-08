#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 16:02:58 2021

@author: cris
"""
def costo_camion(): 
    f = open("Data/camion.csv", "rt")
    headers = next(f).split(",")
    resultado = 0.0
    for line in f: 
        row = line.split(",")
        sumar = int(row[1])*float((row[2]))
        resultado += sumar
    f.close()
    return resultado
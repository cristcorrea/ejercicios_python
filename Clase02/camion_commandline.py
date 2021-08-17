#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 23:32:03 2021

@author: cris
"""
#camion_commandline.py
import csv
import sys
def costo_camion(nombre_archivo): 
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    resultado = 0
    for i,line in enumerate(rows): 
        try:
            sumar = int(line[1])*float((line[2]))
            resultado += sumar
        except:
            print("Fila {} faltan datos".format(i+1))
    f.close()
    return resultado

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = "Data/camion.csv"
    

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)
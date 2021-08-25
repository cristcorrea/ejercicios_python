#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 16:02:58 2021

@author: cris
"""
import csv
def costo_camion(nombre_archivo): 
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    resultado = 0
    for i,line in enumerate(rows, start=1): 
        record = dict(zip(headers, line))
        try:
           ncajones = int(record['cajones'])
           precio = float(record['precio'])
           resultado += ncajones * precio
        except:
            print("Fila {}. No se puede interpretar: {}".format(i+1, line))
        print(record)
    return resultado


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 09:25:15 2021

@author: cris
"""

import csv

def leer_camion(): 
    f = open('../Data/fecha_camion.csv')
    rows = csv.reader(f)
    headers = next(rows)
    precio_camion = 0
    camion = []
    for i, line in enumerate(rows, start=1):
        record = dict(zip(headers, line))
        try:
           ncajones = int(record['cajones'])
           precio = float(record['precio'])
           precio_camion += ncajones * precio
        except:
            print('Linea {} (leer_camion) no se puede comprender: {}'.format(i+1, line))
        camion.append(record)        
    return precio_camion, camion

def leer_precios():
    f = open('../Data/precios.csv')
    rows = csv.reader(f)
    precios_dic = {}
    for i, row in enumerate(rows):
        try:
            precios_dic[row[0]] = float(row[1])
        except:
            print('Linea {} (leer_precios) no se puede comprender: {}'.format(i+1, row))
    return precios_dic 



precio_camion = leer_camion()
precios = leer_precios()


recaudado = 0.0
for i,j in enumerate(precio_camion[1]):
    ncajones = int(j['cajones'])
    precio = float(precios[j['nombre']])
    recaudado += ncajones * precio
        
        
diferencia = recaudado - precio_camion[0]
print(f'Costo total del camión: {precio_camion[0]}')
print('Total recaudado:', recaudado)
print('Diferencia:', round(diferencia,2))


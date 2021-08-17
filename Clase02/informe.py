#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 09:25:15 2021

@author: cris
"""

import csv

def leer_camion(): 
    f = open('Data/camion.csv')
    rows = csv.reader(f)
    headers = next(rows)
    camion = []
    for i, line in enumerate(rows):
        lote = {'nombre': line[0], 'cajones': int(line[1]), 'precio': float(line[2])}
        camion.append(lote)
    return camion

def leer_precios(): 
    f = open('Data/precios.csv')
    rows = csv.reader(f)
    precios_dic = {}
    for i, row in enumerate(rows):
        try:
            precios_dic[row[0]] = float(row[1])
        except:
            print('Linea {} de lista de precios en blanco\n'.format(i+1))
    return precios_dic

camion = leer_camion()
precios = leer_precios()

costo_camion = 0.0
for producto in camion:
    costo_camion += producto['cajones']*producto['precio']

recaudado = 0.0
for i,j in enumerate(camion):
    busqueda = camion[i]['nombre']
    if busqueda in precios:
        recaudado += camion[i]['cajones']*precios[busqueda]
        
    
diferencia = recaudado - costo_camion
print('Costo total del camión:', costo_camion )
print('Total recaudado:', recaudado)
print('Diferencia:', round(diferencia,2))


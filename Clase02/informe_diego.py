# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 18:23:14 2021

@author: Admin
"""

import csv
import sys

def leer_precios(precios_archivo):
    precios_dict = {}
    p = open(precios_archivo)
    rows = csv.reader(p)
    for row in rows:
        if(row):
            precios_dict [row[0]] = row[1]
    return (precios_dict)
    
    
def leer_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = (row[0], int(row[1]), float(row[2]))
            camion.append(lote)
    return camion

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'camion.csv'
    
precios_dict = leer_precios('precios.csv')
camion_lista = leer_camion(nombre_archivo)
ventas = 0
costo = 0
for producto in camion_lista:
    costo += int(producto[1]) * float(producto[2])
    ventas +=  int(producto[1]) * float(precios_dict[producto[0]])
print('Balance del negocio\n')
print(f'Costo: {costo}\nVentas: {ventas}\nDiferencia: {ventas-costo}')
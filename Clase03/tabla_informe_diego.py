# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 18:23:14 2021

@author: Admin
"""

import csv
import sys

 #%% Crea un diccionario con precios
def leer_precios(precios_archivo):
    precios_dict = {}
    p = open(precios_archivo)
    rows = csv.reader(p)
    for row in rows:
        if(row):
            precios_dict [row[0]] = row[1]
    return (precios_dict)
    
 #%% Crea una lista de diccionarios
def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = (row[0], int(row[1]), float(row[2]))
            camion.append(lote)
    return camion


 #%% 
def hacer_informe(lista_camion,dict_precios):
    informe = []
    for row in lista_camion:
        l = (row[0], int(row[1]), float(row[2]),float(dict_precios[row[0]])-row[2])
        informe.append(l)
    return (informe)

 #%%    
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'
    
precios = leer_precios('../Data/precios.csv')
camion = leer_camion(nombre_archivo)
informe = hacer_informe(camion,precios)
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
guion = '-'
print('%10s %10s %10s %10s' % headers)
print(f'{guion:->10s} {guion:->10s} {guion:->10s} {guion:->10s}')
for nombre, cajones, precio, cambio in informe:
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')

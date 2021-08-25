#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 15:50:07 2021

@author: cris
"""

import csv

def leer_camion(): 
    f = open('../Data/camion.csv')
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
    return camion

def leer_precios():
    f = open('../Data/precios.csv')
    rows = csv.reader(f)
    precios_dic = {}
    for i, row in enumerate(rows):
        try:
            precios_dic[row[0]] = float(row[1])
        except:
            print('Linea {} (leer_precios) no se puede comprender: {}\n'.format(i+1, row))
    return precios_dic 


def hacer_informe(precio_camion, precios):
    lista = []
    for cajon in precio_camion:
        s = (cajon['nombre'], int(cajon['cajones']), float(cajon['precio']), float(precios[cajon['nombre']])-float(cajon['precio']))
        lista.append(s)
    return lista

precio_camion = leer_camion()
precios = leer_precios()
informe = hacer_informe(precio_camion, precios)

headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
print("{:>10s} {:>10s} {:>10s} {:>10s}".format(headers[0], headers[1], headers[2], headers[3]))
print("{:->10} {:->10} {:->10} {:->10}.".format("", "", "", ""))
for nombre, cajones, precio, cambio in informe:
    print(f'{nombre:>10s} {cajones:>10d} {"$":>5}{precio:>.2f} {cambio:>10.2f}')
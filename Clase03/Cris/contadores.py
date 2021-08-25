#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 14:52:13 2021

@author: cris
"""

import csv

def leer_camion(nombre_archivo): 
    f = open(nombre_archivo)
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

camion_leido = leer_camion('../Data/camion.csv')
camion_leido2 = leer_camion('../Data/camion2.csv')
from collections import Counter
tenencias = Counter()
tenencias2 = Counter()
for s in camion_leido[1]:
    tenencias[s['nombre']] += int(s['cajones'])
for s in camion_leido2[1]:
    tenencias2[s['nombre']] += int(s['cajones'])  
combinada = tenencias + tenencias2

    
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 16:27:16 2021

@author: Admin
"""

import csv

def costo_camion(nombre_archivo):
    f = open(nombre_archivo)
    costo_total=0
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        try:
            costo_unitario =int(row[1]) * float(row[2])
            costo_total += costo_unitario
        except:
            print(f'{row[0]} tiene datos faltantes')
    return(costo_total)   

costo = costo_camion('missing.csv')
print('Costo total:', costo)

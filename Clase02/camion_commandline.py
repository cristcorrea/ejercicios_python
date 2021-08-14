# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 15:52:58 2021

@author: Admin
"""

import csv
import sys

def costo_camion(nombre_archivo):
    f = open(nombre_archivo)
    costo_total=0
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        costo_unitario =int(row[1]) * float(row[2])
        costo_total += costo_unitario
    return(costo_total)  
  
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)
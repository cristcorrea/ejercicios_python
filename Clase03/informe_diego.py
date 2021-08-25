# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 16:27:16 2021

@author: Admin
"""

import csv

def costo_camion(nombre_archivo):
    f = open(nombre_archivo)
    costo_total=0
    filas = csv.reader(f)
    encabezados = next(filas)
    for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezados, fila))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo_total += ncajones * precio
            # Esto atrapa errores en los int() y float() de arriba.
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return(costo_total)   

costo = costo_camion('fecha_camion.csv')
print('Costo total:', costo)
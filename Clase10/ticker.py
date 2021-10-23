#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 00:37:20 2021

@author: cris
"""

from formato_tabla import crear_formateador
from vigilante import vigilar
import csv

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))
        
def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]
        

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

def filtrar_datos(rows, nombres):
    for row in rows:
        if row['nombre'] in nombres:
            yield row
            
def ticker(camion_file, log_file, fmt):
    lines = vigilar(log_file)
    

if __name__ == '__main__':
    lines = vigilar('../Data/mercadolog.csv')
    rows = parsear_datos(lines)
    for row in rows:
        print(row)
        

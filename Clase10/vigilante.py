#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 22:20:49 2021

@author: cris
"""

# vigilante.py
import os
import time

def vigilar(archivo):
    ''' Lee la última línea generada por "sim_mercado.py" ,que se encuentra
    en ejecución, y devuelve un string con nombre, precio y volumen'''
    f = open(archivo)
    f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF
    
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)   # Esperar un rato y
            continue          # vuelve al comienzo del while
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])
        if volumen > 1000:
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')
        
        
if __name__ == '__main__':
    ''' Devuelve la última linea generada por "sim_mercado.py" si el producto
    está dentro de la lista de "camion.csv"'''
    import informe_final
    
    camion = informe_final.leer_camion ('../Data/camion.csv')

    for line in vigilar('../Data/mercadolog.csv'):  
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])

        if nombre in camion:    
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')
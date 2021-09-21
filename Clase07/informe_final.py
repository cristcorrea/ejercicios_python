#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 09:27:59 2021

@author: cris
"""
'''
En este archivo debería abrir el csv para enviar el contenido a fileparse.
NO FUNCIONA 
'''
import fileparse as fp
import sys


def leer_camion(archivo_camion):
    with open(archivo_camion) as lineas_camion:
        lectura_camion = fp.parse_csv(lineas_camion, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])      
    return lectura_camion

def leer_precios(archivo_precios):
    with open(archivo_precios) as lineas_precios:
        lectura_precios = dict(fp.parse_csv(lineas_precios, types = [str, float], has_headers = False))
    return lectura_precios


def hacer_informe(precio_camion, precios):
    lista = []
    for cajon in precio_camion:
        s = (cajon['nombre'], int(cajon['cajones']), float(cajon['precio']), float(precios[cajon['nombre']])-float(cajon['precio']))
        lista.append(s)
    return lista

def informe_funciones(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print('%10s %10s %10s %10s'  % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in informe:
        print('%10s %10d %10.2f %10.2f' % row)

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    precio_camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(precio_camion, precios)
    informe_funciones(informe)
    
def f_principal(argumento):
    # if len(sys.argv) != 3:
    #     raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios')
    camion = argumento[1]
    precios = argumento[2]
    informe_camion(camion, precios)
    
if __name__ == '__main__':
    f_principal(sys.argv)


    
    


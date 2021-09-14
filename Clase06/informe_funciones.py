#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 09:27:59 2021

@author: cris
"""

import fileparse as fp

def leer_camion(archivo_camion): 
    camion = fp.parse_csv(archivo_camion, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])      
    return camion

def leer_precios(archivo_precios):
    lista_precios = dict(fp.parse_csv(archivo_precios, types = [str, float], has_headers = False))
    return lista_precios 


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

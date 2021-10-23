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
import lote
import formato_tabla


def leer_camion(archivo_camion):
    with open(archivo_camion) as lineas_camion:
        camion_dicts = fp.parse_csv(lineas_camion, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    lectura_camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
    return lectura_camion

def leer_precios(archivo_precios):
    with open(archivo_precios) as lineas_precios:
        lectura_precios = dict(fp.parse_csv(lineas_precios, types = [str, float], has_headers = False))
    return lectura_precios


def hacer_informe(precio_camion, precios):
    lista = []
    for cajon in precio_camion:
        s = (cajon.nombre, int(cajon.cajones), float(cajon.precio), float(precios[cajon.nombre])-float(cajon.precio))
        lista.append(s)
    return lista

def imprimir_informe(informe, formateador):
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)

def informe_camion(nombre_archivo_camion, nombre_archivo_precios, fmt):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es .txt
    Alternativas: .csv o .html
    '''
    precio_camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    # Obtiene los datos para un informe
    informe = hacer_informe(precio_camion, precios)
    # Imprimir 
    formateador = formato_tabla.crear_formateador(fmt) 
    imprimir_informe(informe, formateador)
    
def f_principal(argumento):
    if len(sys.argv) != 4:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios')
    camion = argumento[1]
    precios = argumento[2]
    fmt = argumento[3]
    informe_camion(camion, precios, fmt)
    
if __name__ == '__main__':
    f_principal(sys.argv)


    
    


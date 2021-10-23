#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:40:24 2021

@author: cris
"""

# fileparse.py

import csv

def parse_csv(files, select = None, types = None, has_headers = True, silence_errors = False):
    '''
    Recibe una serie de lineas y entrega una lista con el contenido. 
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, 
    que debe ser una lista de nombres de las columnas a considerar.
    FUNCIONA
    '''
    filas = csv.reader(files)
    if select != None and has_headers == False:
        raise RuntimeError ('Para seleccionar, necesito encabezados')

    if has_headers:
        # Lee los encabezados del archivo
        encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []
        
        registros = []
        for indice, fila in enumerate(filas, start=1):
            try:
                if not fila:    # Saltear filas vacías
                    continue
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]
                # Filtra la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
            except ValueError as e:
                if silence_errors == False:
                    print(f'Fila {indice}: No pude convertir: {fila}')
                    print(f'Fila {indice}:', e)                   
    else: ## aca arma lista de tuplas porq no tiene encabezados
        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            if types:
                fila = [func(val) for func, val in zip(types, fila) ]
            # Armar tuplas
            registros.append(tuple(fila))
    return registros



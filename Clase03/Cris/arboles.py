#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 23:36:16 2021

@author: cris
"""

import csv
from collections import Counter

lista = []

def leer_parque(nombre_archivo, parque):
    global lista 
    with open(nombre_archivo, encoding="utf8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        numero_arboles = 0
        for row in rows:
            arboles = {}
            arboles = dict(zip(headers, row))
            if arboles['espacio_ve'] == parque:
                lista.append(arboles)
                numero_arboles = numero_arboles + 1
    return numero_arboles

def especies(lista_especies):
    listado = set()
    for i in lista_especies:
       espec = i['nombre_com']
       listado.add(espec)  
    return (listado)

def contar_ejemplares(lista_especies):
   cantidad = []
   for i in lista_especies:
       contar = i['nombre_com']
       cantidad.append(contar)
   cant_arboles = Counter(cantidad)      
   secuencia = cant_arboles.most_common(5)
   return(secuencia)

def obtener_alturas(lista_especies, nombre_comun):
    alturas=[]
    suma = 0.0
    muestras = 0
    mostrar = {}
    for i in lista_especies:
        contar = i['altura_tot']
        if i['nombre_com'] == nombre_comun:
            alturas.append(float(contar))
    for i in alturas:
        suma += i
        muestras = muestras + 1
    promedio =round((suma/muestras),2)
    maximo = alturas[0]
    for i in range(1, len(alturas)):
        if alturas[i] > maximo:
            maximo = alturas[i]
    minimo = alturas[0]
    for i in range(1, len(alturas)):
        if alturas[i] < minimo:
            minimo = alturas[i]
    mostrar['Promedio:'] = promedio
    mostrar['Máximo:'] = maximo
    mostrar['Minimo:'] = minimo 
    return(mostrar)

#%%

def leer_arboles(nombre_archivo):
    with open(nombre_archivo, encoding="utf8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        arboleda = []
        for row in rows:
            arbol = {name:s for name, s in zip(headers, row)}
            arboleda.append(arbol)
    return arboleda
        
arboleda = leer_arboles('../Data/arbolado.csv')
H = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

























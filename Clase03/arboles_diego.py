# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 23:33:45 2021

@author: Admin
"""

import csv
from pprint import pprint

#%%
def leer_parque(nombre_archivo, parque):
    
    arboles=[]
    registro={}
    with open(nombre_archivo,"rt",encoding="utf8") as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        encabezados 
        for n_fila,fila in enumerate (filas,start=0):
            registro = dict(zip(encabezados, fila)) 
            if  registro['espacio_ve']== parque:
                arboles.append(registro)
        print(len(arboles))
    return arboles

#%%
def leer_arboles(nombre_archivo):
    
    arboles=[]
    registro={}
    with open(nombre_archivo,"rt",encoding="utf8") as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        encabezados 
        for fila in filas:
            registro = dict(zip(encabezados, fila)) 
            arboles.append(registro)
                
    return arboles


#%%

def especies(lista_arboles):
    especies=set([])
    for arbol in lista_arboles:
       especies.add(arbol["nombre_com"])
    
    return especies

#%%

def contar_ejemplares(lista_arboles):
    from collections import Counter
    tenencias = Counter()
    cont_especies=[]
    for arbol in lista_arboles:
       tenencias[arbol['nombre_com']] += 1
       
    cont_especies.append(tenencias)
    print("-",arbol['espacio_ve'])
    print(tenencias.most_common(5))
    
    return cont_especies
    
#%%

# EJERCICIOS
archivo = "../Data/arbolado-en-espacios-verdes.csv"

#Ejercicio 3.18
arboles = leer_parque(archivo,"GENERAL PAZ")

#Ejercicio 3.19: Determinar las especies en un parque
especies=especies(arboles)
#pprint(especies)


#Ejercicio 3.20: Contar ejemplares por especie
contar_ejemplares=contar_ejemplares(arboles)
#pprint(contar_ejemplares)


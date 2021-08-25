#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 18:58:56 2021

@author: cris
"""
#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error estaba en el else, que hacía salir del bucle. 
#Lo corregí quitandolo. También agregue la A (mayúscula). 
#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    respuesta = False
    while i<n:
        if expresion[i] in 'aA':
            respuesta = True
        i += 1
    return respuesta

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.2. Función tiene_a()
#Comentario:Faltaban los dos puntos luego del while y el if y el doble igual en la
#comparación. 
#Lo corregí agregando lo faltante e incluyendo la A mayúscula. 
#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] in 'aA':
            return True
        i += 1
    return Falso

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')
#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: No admitía enteros como parámetro. 
#Lo corregí declarando el parámetro como String 
#    A continuación va el código corregido
def tiene_uno(expresion):
    palabra = str(expresion)
    n = len(palabra)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if palabra[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)
#%%
#Ejercicio 3.4. Función suma()
#Comentario: Faltaba colocar el return de la función 
# Se solucionó solo con colocar return c en la función 
#    A continuación va el código corregido
def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")
#%%
#Ejercicio 3.4. Función suma()
#Comentario: el diccionario registro estaba mal ubicado.
#Se solucionó al colocar el dicc registro dentro del bucle for
#    A continuación va el código corregido
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
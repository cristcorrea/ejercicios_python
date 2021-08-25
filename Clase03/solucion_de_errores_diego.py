# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 22:19:04 2021

@author: Admin
"""

#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era semantico y estaba ubicado en la linea 20
#    Lo corregí devolviendo false cuando no encontro 'Aa'.
#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] in 'aA':
            return True
        i += 1
    return False
        

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era sintactico y estaba ubicado en el final de las expresiones
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.
def tiene_uno(expresion):
    n = len(str(expresion))
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

#%%
#Ejercicio 3.4. Función suma()
#Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.
def suma(a,b):
    c = a + b
    print(f"La suma da {a} + {b} = {c}")



#%%
#Ejercicio 3.5. Función leer_camion()
#Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion
#%%
camion = leer_camion('camion.csv')
pprint(camion)
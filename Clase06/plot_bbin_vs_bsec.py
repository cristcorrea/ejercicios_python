#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 17:32:53 2021

@author: cris
"""
import random
import matplotlib.pyplot as plt
import numpy as np
import bbin 


def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps



def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0, m-1)

# m = 10000
# n = 100
# k = 1000


def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += bbin.busqueda_binaria(lista,x)
    comps_prom = comps_tot / k
    return comps_prom

largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
comp_sec_prom = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
comp_bin_prom = np.zeros(256)   

def graficar_bbin_vs_bseq(m, k):
    for i, n in enumerate(largos):
        lista = generar_lista(n,m)
        comp_sec_prom[i] = experimento_secuencial_promedio(lista, m, k)
        comp_bin_prom[i] = experimento_binario_promedio(lista, m, k) 
    
    # ahora grafico largos de listas contra operaciones promedio de búsqueda.
    plt.subplot(1,2,1)
    plt.plot(largos,comp_sec_prom,label = 'Búsqueda Secuencial')
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de la Búsqueda")
    plt.legend()
    plt.subplot(1,2,2)
    plt.plot(largos,comp_bin_prom,label = 'Búsqueda Binaria')
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de la Búsqueda")
    plt.legend()
    plt.show()


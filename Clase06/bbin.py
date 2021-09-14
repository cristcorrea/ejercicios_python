#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 14:28:21 2021

@author: cris
"""
    
def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos

def donde_insertar(lista, x):
    '''Donde insertar
    Precondición: la lista está ordenada
    Devuelve la posición donde se podría insertar el
    elemento para que la lista permanezca ordenada'''
    pos = 0
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] <= x and lista[medio+1] > x:
            pos = medio     # posición encontrada!
        if lista[medio] < x and lista[medio+1] >= x:
            pos = medio+1     # posición encontrada! 
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos

def insertar(lista, x):
    ''' Insertar
    Precondicón: la lista está ordenada
    Devuelve la posición donde se encuentra el elemento, 
    si el elemento no está lo inserta donde corresponde para mantener
    el orden y devuelve la posición'''
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    if x in lista:
        while izq <= der:
            medio = (izq + der) // 2
            if lista[medio] == x:
                pos = medio     # elemento encontrado!
                break
            if lista[medio] > x:
                der = medio - 1 # descarto mitad derecha
            else:               # if lista[medio] < x:
                izq = medio + 1 # descarto mitad izquierda
    else:
        while izq <= der:
            medio = (izq + der) // 2
            if lista[medio] <= x and lista[medio+1] > x:
                pos = medio     # posición encontrada!
            if lista[medio] < x and lista[medio+1] >= x:
                pos = medio+1     # posición encontrada!
            if lista[medio] > x:
                der = medio - 1 # descarto mitad derecha
            else:               # if lista[medio] < x:
                izq = medio + 1 # descarto mitad izquierda
        lista.insert(pos, x)
    return pos

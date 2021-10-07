#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 18:39:14 2021

@author: cris
"""
import os
import sys


def archivos_png(directorio):
    '''Recibe un directorio y devuelve una lista con 
    los archivos del tipo .png que contenga el directorio y
    los subdirectorios del mismo.'''
    lista = []
    for roots, dirs, file in os.walk(directorio):
        for name in file:
            if 'png' in name:
                lista.append(name)
    return lista

if __name__ == '__main__':
    nombre_archivo = sys.argv[1]
    print(archivos_png(nombre_archivo))
    

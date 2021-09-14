#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 16:02:58 2021

@author: cris
"""
import csv
import informe_funciones as infor
def costo_camion(nombre_archivo): 
    resultado = 0
    camion = infor.leer_camion(nombre_archivo)
    for i, cajon in enumerate(camion):
        try:
           ncajones = int(camion[i]['cajones'])
           precio = float(camion[i]['precio'])
           resultado += ncajones * precio
        except:
            print("Fila {}. No se puede interpretar: {}".format(i+1, cajon))
    return resultado


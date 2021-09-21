#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 16:02:58 2021

@author: cris
"""

import informe_final as infor
import sys


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
    print(resultado)
    return resultado

def f_principal(argumento):
    valor = costo_camion(argumento[1])
    return valor 
    
if __name__ == '__main__':
    f_principal(sys.argv)

#prueba = costo_camion('../Data/camion.csv')

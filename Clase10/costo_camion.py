#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 16:02:58 2021

@author: cris
"""

import informe_final as infor


def costo_camion(nombre_archivo): 
    camion = infor.leer_camion(nombre_archivo)
    return camion.precio_total()

def f_principal(argumento):
    valor = costo_camion(argumento[1])
    return valor 
    
if __name__ == '__main__':
    import sys
    f_principal(sys.argv)


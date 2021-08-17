#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 14:25:37 2021

@author: cris
"""

import csv
def leer_precios(nombre_archivo): 
    f = open(nombre_archivo)
    rows = csv.reader(f)
    precios_dic = {}
    for i, row in enumerate(rows):
        try:
            precios_dic[row[0]] = float(row[1])
        except:
            print('Linea {} en blanco'.format(i+1))
    return precios_dic
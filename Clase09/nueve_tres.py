#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 00:01:13 2021

@author: cris
"""
import lote
import fileparse

with open('../Data/camion.csv') as lineas:
    camion_dicts = fileparse.parse_csv(lineas, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    
camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]


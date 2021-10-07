# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 22:04:49 2021

@author: Admin
"""
import os


def archivos_png(directorio):
    archivos_png=[]
    for root, dirs, files in os.walk(directorio):
        for name in files:
            if name.endswith('.png'):
                archivos_png.append(name)
        for name in dirs:
            if name.endswith('.png'):
                archivos_png.append(name)
    print(archivos_png)
    return 



directorio = '..\Data\ordenar'
archivos_png(directorio)

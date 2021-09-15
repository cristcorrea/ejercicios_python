# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 21:59:00 2021

@author: Admin
"""
import random
import numpy as np


def crear_album(figus_total):
    album = np.zeros(figus_total)
    return (album)

def album_incompleto(album):
    return (0 in album) 

def comprar_figu(figus_total):
    
    return (random.randint(1, figus_total))

def cuantas_figu(figus_total):
    album=crear_album(figus_total)
    figus_compradas=0
    while(album_incompleto(album)):
        figu=comprar_figu(figus_total)
        album[figu-1] += 1
        figus_compradas += 1
    return figus_compradas


figus_total=670
print(cuantas_figu(figus_total))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 23:47:38 2021

@author: cris
"""

def propagar_a_derecha(l):
    n = len(l)
    nueva_l = l.copy()
    for i,e in enumerate(nueva_l):
        if e==1 and i<n-1:
            if nueva_l[i+1]==0:
                nueva_l[i+1] = 1
    return nueva_l
#%
def propagar_a_izquierda(l):
    return propagar_a_derecha(l[::-1])[::-1]
#%
def propagar(l):
    ld=propagar_a_derecha(l)
    lp=propagar_a_izquierda(ld)
    return lp
#%%
l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
print("Estado original:  ",l)
print("Porpagando...")
lp=propagar(l)
print("Estado original:  ",l)
print("Estado propagado: ",lp)
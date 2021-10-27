#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 15:39:49 2021

@author: cris
"""

def medidas_hoja_A(N, val_ant = None):
    '''Pre = pasar un entero positivo como parámetro'''
    A0 = [841, 1189] 
    if N == 0 and val_ant == None: # Si el tamaño consultado es A0, retorna A0
        res = tuple(A0)
    elif N == 0: # Si N llega a valer 0, entonces devuelve la medida "val_ant"
        res = tuple(val_ant)
    else:
        if val_ant == None: # Por defecto si N != 0 asigna valor a val_ant
            val_ant = A0
        val_ant = val_ant[::-1] # Invierte los valores 
        val_ant[0] = val_ant[0]//2 # Divide al primer número por 2
        res = medidas_hoja_A(N-1, val_ant) # Realiza la recursión 
        
    return res
        
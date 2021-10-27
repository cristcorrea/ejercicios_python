#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 15:39:49 2021

@author: cris
"""

def medidas_hoja_A(N, val_ant = None):
    
    A0 = [841, 1189]
    if N == 0 and val_ant == None:
        res = tuple(A0)
    elif N == 0:
        res = tuple(val_ant)
    else:
        if val_ant == None:
            val_ant = A0
        val_ant = val_ant[::-1]
        val_ant[0] = val_ant[0]//2
        res = medidas_hoja_A(N-1, val_ant)
        
    return res
        
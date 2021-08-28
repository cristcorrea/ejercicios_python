#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 08:26:52 2021

@author: cris
"""

def buscar_u_elemento(lista, u):
    pos = -1
    for i, j in enumerate(lista): 
        if j == u:
            pos = i
    return pos
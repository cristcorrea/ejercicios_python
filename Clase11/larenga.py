#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 20:03:37 2021

@author: cris
"""

def pascal(n, k):
    ''' Fila n, posición k, con n=0 y k=0'''
    
    if k == 0 or n == k:
        res = 1
        return res
    return pascal(n-1, k-1) + pascal(n-1, k)
    
    
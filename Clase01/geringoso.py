#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 10:42:54 2021

@author: cris
"""

cadena = 'Geringoso'
capadepenapa = ''
for c in cadena:
        if c in "aeiouAEIOU": 
            capadepenapa += c
            capadepenapa += "p"
        capadepenapa += c
print(capadepenapa)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 12:10:28 2021

@author: cris
"""
personas = 30
i = 0
proba = 1
for  persona in range(personas):
    proba *= (365-i)/365
    i += 1
    print(i,(1-proba)*100)
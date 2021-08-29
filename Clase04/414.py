#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 17:46:53 2021

@author: cris
"""
import csv

f = open('../Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)

def fecha_t(fecha):
    fecha_tupla = fecha.split('/')
    out = tuple(int(s) for s in fecha_tupla)
    return out
    

types = [str, float, fecha_t, str, float, float, float, float, int]
converted = [func(val) for func, val in zip(types, row)] 
record = dict(zip(headers, converted))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 16:02:58 2021

@author: cris
"""
f = open("Data/camion.csv", "rt")
headers = next(f).split(",")
for line in f: 
    row = line.split(",")
    print(row)
f.close()
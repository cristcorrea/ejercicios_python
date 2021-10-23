#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 13:17:10 2021

@author: cris
"""

class Camion:
    
    def __init__(self, lotes):
        self.lotes = lotes
        
    def __iter__(self):
        return self.lotes.__iter__()
    
    def __contains__(self, nombre):
        return any([lote.nombre == nombre for lote in self.lotes])
    
    def __len__(self):
        return len(self.lotes)
    
    def __getitem__(self, i):
        return self.lotes.__getitem__(i)
    
    def __str__(self):
        imprimir = ''
        print(f'Camión con {self.lotes.__len__()} lotes:')
        for i,lote in enumerate(self.lotes):
            imprimir += (f'{self.lotes[i]}') + '\n'
        return imprimir

    
    def __repr__(self):
        imprimir = ''
        print(f'Camión con {self.lotes.__len__()} lotes:')
        for i,lote in enumerate(self.lotes):
            imprimir += (f'{self.lotes[i]}') + '\n'
        return imprimir 
            
    def precio_total(self):
        ''' Devuelve el precio total del camión'''
        return sum([l.costo() for l in self.lotes])
    
    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
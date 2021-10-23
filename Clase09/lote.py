#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 23:20:07 2021

@author: cris
"""

class Lote():
    
    def __init__(self, nombre , cajones , precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
    
    def __repr__(self):
        return f'Lote({self.nombre},{self.cajones},{self.precio})'
    
    def __str__(self):
        return f'(Lote de {self.lotes.cajones} cajones de {self.lotes.nombre}, pagados a ${self.lotes.precio} cada uno)'
        
    def costo(self):
        return self.cajones*self.precio
    
    def vender(self, cantidad):
        self.cajones -= cantidad
        
        
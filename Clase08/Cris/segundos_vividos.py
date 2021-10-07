#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 16:20:09 2021

@author: cris
"""
import datetime


def vida_en_segundos(fecha_nac):
    '''le pasás tu fecha de nacimiento y te devuelve 
    la cantidad de segundos que viviste 
    (asumiendo que naciste a las 00:00hs de tu fecha de nacimiento)
    '''
    nacimiento = datetime.datetime.strptime(fecha_nac, '%d/%m/%Y')
    fecha_actual = datetime.datetime.today()
    edad = (fecha_actual - nacimiento).total_seconds()
    
    return edad



valor = vida_en_segundos('30/11/1988')
print(valor)


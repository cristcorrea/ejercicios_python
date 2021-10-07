#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 16:20:09 2021

@author: cris
"""
import datetime


def vida_en_segundos(fecha_nac):
    '''Recibe una fecha de nacimiento del tipo '30/11/1988' y devuelve 
    la cantidad de segundos que viviste 
    (asumiendo que naciste a las 00:00hs de tu fecha de nacimiento)
    '''
    nacimiento = datetime.datetime.strptime(fecha_nac, '%d/%m/%Y')
    fecha_actual = datetime.datetime.today()
    edad = float((fecha_actual - nacimiento).total_seconds())
    
    return edad

#%%

def cuanto_falta():
    hoy = datetime.date.today()
    primavera = datetime.date(2022, 9, 21)
    faltan_dias = primavera - hoy
    return faltan_dias.days
    
#%%

def reincorporacion(dias):
    desde = datetime.date(2020, 9, 26)
    reingreso = desde + datetime.timedelta(days=dias)
    return reingreso


    
    
    
    
    
    
    
    
    
    
    
    
    
    
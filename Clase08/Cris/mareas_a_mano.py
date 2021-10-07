#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 12:48:05 2021

@author: cris
"""

import pandas as pd

# Creo el dataframa
df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv')
# Cambio el índice de posición por la columna Time
df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)

#Creo una copia 
dh = df['12-25-2014':].copy()

'''Estimo la diferencia entre ceros para ambos puertos como el 
el cociente entre la diferencia de las sumatorias y la cantidad de mediciones'''
diferencia = ((dh['H_SF'].sum()) - (dh['H_BA'].sum()))/168

''' En el caso de delta_t revisé el gráfico inicial y observé diferencia de una hora
entre las valores maximo y minimos de las mareas
También googleando encontré que la vel. de propagación de la marea hacia el 
interior del Río de La Plata es de 30 Km/h aprox., y la distancia entre ambos puertos
es de aprox 25 Km, por lo cual 1 hora de diferencia parece lo correcto'''

delta_t = -1 # tiempo que tarda la marea entre ambos puertos


delta_h = diferencia # diferencia de los ceros de escala entre ambos puertos

pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 10:45:28 2021

@author: cris
"""

import pandas as pd
import os
import seaborn as sns

directorio = '../Data'
archivo = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio,archivo)
df_lineal = pd.read_csv(fname)
cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
df_lineal_sel = df_lineal[cols_sel]

#%%
cant_ejemplares = df_lineal_sel['nombre_cientifico'].value_counts().head(10)
print(cant_ejemplares)

#%%
especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]

df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')
df_lineal_seleccion.boxplot('altura_arbol', by = 'nombre_cientifico')
#%%
sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')

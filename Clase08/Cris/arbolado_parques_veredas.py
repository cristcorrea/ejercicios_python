#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 11:37:35 2021

@author: cris
"""

import pandas as pd
import os


#%%
# Creo los dataframes 
directorio = '../Data'
archivo1 = 'arbolado-publico-lineal-2017-2018.csv'
archivo2 = 'arbolado.csv'
fveredas = os.path.join(directorio,archivo1)
fparques = os.path.join(directorio,archivo2)
df_parques = pd.read_csv(fparques)
df_veredas = pd.read_csv(fveredas)
#%%
# Creo otros DF con la especie seleccionada Tipuana Tipu y Tipuana tipu
df_tipas_parques = df_parques[df_parques['nombre_cie'].isin(['Tipuana Tipu'])]
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'].isin(['Tipuana tipu'])]

#%%
# Selecciono las columas que quiero ver 
df_tipas_p = df_tipas_parques[['altura_tot', 'diametro']].copy()
df_tipas_v = df_tipas_veredas[['altura_arbol', 'diametro_altura_pecho']]

# Renombro las columnas en el DF veredas para unificar nombres 
df_tipas_v = df_tipas_v.rename(columns={"altura_arbol": "altura_tot", "diametro_altura_pecho": "diametro"}).copy()

# Agrego una columna 'ambiente' que describe el lugar donde se haya plantado el árbol
df_tipas_p = df_tipas_p.assign(ambiente = 'parque')
df_tipas_v = df_tipas_v.assign(ambiente = 'vereda')

# Junto ambos dataframes 
df_tipas = pd.concat([df_tipas_v, df_tipas_p])
#%%
# Crep un boxplot para alturas y diámetro 
df_tipas.boxplot('diametro',by = 'ambiente')
df_tipas.boxplot('altura_tot',by = 'ambiente')

#%%
'''
¿Qué tendrías que cambiar para repetir el análisis para otras especies? 

Para repetir el análisis con otra especie debería modificar el nombre científico 
en los siguientes DF:
    
df_tipas_parques = df_parques[df_parques['nombre_cie'].isin(['Tipuana Tipu'])]
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'].isin(['Tipuana tipu'])]

¿Convendría definir una función?

Al no tener los mismos nombres en columnas o especies, por ejemplo, se complica
poder realizar mediante una función la selección de una especie particular'''




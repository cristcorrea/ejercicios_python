#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 14:11:35 2021

@author: cris
"""

import pandas as pd
import seaborn as sns
import os

directorio = '../Data/'#os.getcwd()
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)
df_parques =pd.read_csv(fname)
cols=['altura_tot', 'diametro' ,'nombre_cie']

directorio = '../Data/'#os.getcwd()
archivo = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio,archivo)
df_veredas=pd.read_csv(fname)
cols2=['altura_arbol', 'diametro_altura_pecho' , 'nombre_cientifico']


df_tipas_parques=df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][cols].copy()
df_tipas_veredas=df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'][cols2].copy()
df_tipas_parques=df_tipas_parques.rename(columns={"altura_tot": "altura_arbol", "diametro": "diametro_altura_pecho","nombre_cie":"nombre_cientifico"})
df_tipas_parques = df_tipas_parques.assign(ambiente = "parque")
df_tipas_parques.loc[:,'ambiente'] = "parque"
df_tipas_veredas.loc[:,'ambiente'] = "vereda"
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
 
print(df_tipas.boxplot('diametro_altura_pecho',by = 'ambiente'))
print(df_tipas.boxplot('altura_arbol',by = 'ambiente'))


#¿Qué tendrías que cambiar para repetir el análisis para otras especies?
# ¿Convendría definir una función?
#Cambiar en la fila 27 y 28 del codigo el nombre de otro arbol ,para repetir con otra especie.
#Podria definirse la funcion , que tome como entrada el nombre de la epecie.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 14:24:16 2021

@author: cris
"""

import os
import pandas as pd

#%%

def df_parques(especie):
    '''
    Devuelve un Dataframe con los datos de arbolado en parques
    Se ingresa el nombre de la especie que se quiere analizar
    '''
    path = os.path.join('..', 'Data')
    archivo = 'arbolado-en-espacios-verdes.csv'
    
    df_parques = pd.read_csv(os.path.join(path, archivo))
    df_tipas_parques = df_parques[df_parques['nombre_cie'] == especie]

    
    return df_parques, df_tipas_parques

#%%

def df_veredas(especie):
    '''
    Devuelve un Dataframe con los datos de arbolado en veredas
    '''
    path = os.path.join('..', 'Data')
    archivo = 'arbolado-publico-lineal-2017-2018.csv'
    
    df_veredas = pd.read_csv(os.path.join(path, archivo))
    df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu']
    
    return df_veredas, df_tipas_veredas

#%%

if __name__ == '__main__':
    
    df_parques = df_parques('Tipuana Tipu')
    df_tipas_parques = df_parques[1][['altura_tot', 'diametro']].copy()
    df_tipas_parques = df_tipas_parques.assign(ambiente='parque')

    df_veredas = df_veredas('Tipuana tipu')
    df_tipas_veredas = df_veredas[1][['altura_arbol', 'diametro_altura_pecho']].copy()
    df_tipas_veredas = df_tipas_veredas.rename(columns ={'altura_arbol':'altura_tot', 'diametro_altura_pecho':'diametro'})
    df_tipas_veredas = df_tipas_veredas.assign(ambiente='vereda')
    
    df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
    df_tipas.boxplot('diametro',by = 'ambiente')
    df_tipas.boxplot('altura_tot',by = 'ambiente')
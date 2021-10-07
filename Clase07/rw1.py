#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 13:35:12 2021

@author: cris
"""

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()
#%%
def graficar_caminatas(Ncaminatas, Npasos):
    '''
    Genera Ncaminatas al azar de Npasos y las grafica.
    Grafica además, en subplots distintos, las caminatas que mas y menos...
    se alejaron del inicio.
    '''
    borracho_activo = np.zeros(Npasos)
    max_borracho_activo = 0
    borracho_vago = np.zeros(Npasos)
    max_borracho_vago = 0
    
    plt.figure(figsize = (8,5))  #creo figura
    
    plt.subplot(2, 1, 1)                   #creo subplot de arriba
    for i in range(Ncaminatas):            
        caminata = randomwalk(Npasos)      #grafico caminata del i-esimo borracho
        dist_max = max(abs(caminata))
        plt.plot(caminata)
        
        if i == 0:           #el primero borracho es el mas rápido y mas lento hasta el moento
            borracho_activo = caminata
            max_borracho_activo = dist_max
            borracho_vago = caminata
            max_borracho_vago = dist_max  
            continue
        
        if dist_max > max_borracho_activo:   #Si el nuevo borracho se alejó mas que el mas activo...
            borracho_activo = caminata
            max_borracho_activo = dist_max
    
        elif dist_max < max_borracho_vago:   #Si el nuevo borracho se alejó menos que el menos activo...
            borracho_vago = caminata
            max_borracho_vago = dist_max    
    plt.xticks([])
    plt.title("12 caminatas al azar")
    
    lim = max_borracho_activo * 1.1          # Defino los límites para los gráficos inferiores
    
    
    plt.subplot(2, 2, 3) # Creo subplot de abajo a la izquierda
    plt.title("la caminata que mas se aleja")
    plt.plot(borracho_activo)
    plt.ylim(-lim,lim)
    plt.xticks([])
    
    plt.subplot(2, 2, 4) # Creo subplot de abajo a la derecha
    plt.title("la caminata que menos se aleja")
    plt.plot(borracho_vago)
    plt.ylim(-lim,lim)
    plt.xticks([]), plt.yticks([])
    
    plt.show()
    
    
if __name__ == "__main__":
    Npasos = 100000
    Ncaminatas = 12
    graficar_caminatas(Ncaminatas, Npasos)
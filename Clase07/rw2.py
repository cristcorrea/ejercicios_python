#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 13:50:00 2021

@author: cris
"""

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)
    return pasos.cumsum()

N = 100000

def ploteo_de_caminatas(N, caminatas = 12):
    """ Toma un valor 'N' de pasos, una cantidad 'caminatas' (por default 12)
    de veces que crea una random walk y plotea todas las caminatas juntas y
    la que más se alejó y la que menos se alejó del origen

    Pre: N y caminatas son números enteros
    Post: 3 ploteos en una misma figura con las caminatas

    """

    for i in range(caminatas):

        caminata = randomwalk(N)

        plt.subplot(2, 1, 1)
        plt.plot(caminata)
        plt.xlabel('Tiempo')
        plt.ylabel('Distancia al Origen')
        plt.title('12 Caminatas al azar')
        plt.grid('on')

        if i == 0:               # Esto se cumple sólo en la primer iteración
            mas_alejada = caminata

        elif any(abs(i) > abs(mas_alejada).max() for i in caminata):
            mas_alejada = caminata

        if i == 0:               # Esto se cumple sólo en la primer iteración
            mas_cercana = caminata

        elif any(abs(i) < abs(mas_cercana).min() for i in caminata):
           mas_cercana = caminata


    plt.subplot(2,2,3)
    plt.plot(mas_alejada)
    plt.xlabel('Tiempo')
    plt.ylabel('Distancia al Origen')
    plt.title('La caminata que más se aleja')
    plt.grid()

    plt.subplot(2,2,4)
    plt.plot(mas_cercana)
    plt.xlabel('Tiempo')
    plt.ylabel('Distancia al Origen')
    plt.title('La caminata que menos se aleja')
    plt.grid()

    plt.show()
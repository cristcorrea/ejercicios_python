#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 11:42:49 2021

@author: cris
"""

frase = "Todos, tu tambien"
palabras = frase.split()
frase_t = ""

for palabra in palabras: 
    auxiliar = ""   
    if "," in palabra: 
        if (len(palabra)<=3):
            auxiliar += palabra + " "
        elif(palabra[-3]) == "o" or (palabra[-3]) == "a":
            for i,j in enumerate(palabra):
                if i == len(palabra)-3: 
                    j = "e"
                auxiliar += j
            auxiliar = auxiliar + " "
    else: 
        if(len(palabra) <=2):
            auxiliar += palabra + " "
        elif(palabra[-2]) == "o" or (palabra[-2]) == "a": 
            for i,j in enumerate(palabra):
                if i == len(palabra)-2: 
                    j = "e"
                auxiliar += j
            auxiliar = auxiliar + " "
        else: 
            auxiliar += palabra + " "
    frase_t += auxiliar 
print(frase_t)
        
        

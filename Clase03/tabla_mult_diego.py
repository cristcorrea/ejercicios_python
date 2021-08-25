# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 11:11:41 2021

@author: Admin
"""
print(end='     ')
for n in range(10):   
    print('%3d'%n, end=' ')
print(f'{"-":->44s}')  
  
for n in range(10):   
    print('\n',n,':', end=' ')
    r=0
    for m in range(10):  
        print('%3d'%r, end=' ')
        r += n

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 00:00:13 2021

@author: cris
"""

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0



mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:   
    if mes >= pago_extra_mes_comienzo: 
        while mes <= pago_extra_mes_fin: 
            saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
            total_pagado = total_pagado + pago_mensual + pago_extra
            mes += 1
            print(mes, round(total_pagado,2), round(saldo, 2))
    saldo = saldo * (1+tasa/12) - pago_mensual 
    total_pagado = total_pagado + pago_mensual
    mes += 1
    print(mes, round(total_pagado,2), round(saldo, 2))
print('Total pagado', round(total_pagado, 2), "Meses:", mes)
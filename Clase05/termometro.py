
import random
import numpy as np
#from pprint import pprint

mu =  37.5
sigma = 0.2
mediciones=[]
N=999
random.normalvariate(mu,sigma)
for i in range(N): 
        mediciones.append(random.normalvariate(mu,sigma))



data=np.array(mediciones)
np.save('../Data/Temperaturas', data)
print("Éste es el listado de mediciones")
print("\nValor máximo encontrado=",max(mediciones))
print("Valor mínimo encontrado=",min(mediciones))
print("El promedio de mediciones es=",sum(mediciones)/N)
mediciones.sort()
mediana_val=(N+1)/2
print("La mediana es=",mediciones[int(mediana_val)])

#import matplotlib.pyplot as plt
#plt.hist(mediciones,bins=100)
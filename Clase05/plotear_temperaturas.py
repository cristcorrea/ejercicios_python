import numpy as np
temperaturas = np.load('../Data/Temperaturas.npy')


print("\nValor máximo encontrado=",max(temperaturas))
print("Valor mínimo encontrado=",min(temperaturas))
print("El promedio de mediciones es=",sum(temperaturas)/temperaturas.size)


import matplotlib.pyplot as plt
plt.hist(temperaturas,bins=100)
plt.show()
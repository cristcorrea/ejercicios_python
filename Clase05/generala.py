import random
from collections import Counter
def tirar():
    tirada=[]                   #tirada final
    tirada1=[]
    tirada2=[]
    tirada3=[]
    elegido=0
    veces=0
    for i in range(5):
        tirada1.append(random.randint(1,6)) #Tiro los dados
    n=Counter(tirada1).most_common(1)
    elegido=n[0][0]             #valor que mas se repitio
    veces=n[0][1]               #cantidad de veces que salio el valor
    

    for j in range(veces):
        tirada.append(elegido)  #agrego el valor en la tirada general
    
    for p in range(5-veces):
        tirada2.append(random.randint(1,6)) #Tiro los dados que me sobraron
    for f in tirada2:
        if f==elegido:
            tirada.append(f)
            veces=veces+1
    
    for g in range(5-veces):
        tirada3.append(random.randint(1,6)) #Tiro los dados que me sobraron
    for h in tirada3:
        tirada.append(h)
        veces=veces+1
    return tirada


def es_generala (tirada):
    if(all(x==tirada[0] for x in tirada)):  #Si todos los valores son iguales
        return True
    else:
        return False  


N=10000
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

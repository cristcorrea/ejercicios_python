def geringoso(cadena):
    capadepenapa=''
    for c in cadena:
        capadepenapa += c
        if c in "aeiouAEIOU":
            capadepenapa += 'p' + c
    return(capadepenapa)
        
lista=['banana', 'manzana', 'mandarina']
d={}
for fruta in lista:
    d[fruta] = geringoso(fruta)
print(d)

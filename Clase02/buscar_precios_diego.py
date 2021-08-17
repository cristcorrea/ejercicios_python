def buscar_precios(fruta):
    for line in f:
        row = line.split(',')
        row[0]=row[0].lower()
        if fruta in row:
            print('El precio de',row[0],'es: ' ,row[1])
            return
    print(fruta,'No figura en el listado')
    return


f=open('precios.csv','rt')
buscar_precios(str.lower(input('Ingrese fruta o verdura:')))     
f.close()

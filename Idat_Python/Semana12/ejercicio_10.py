def separarParesImpares(lista):
    listaPares=[]
    listaImpares=[]
    for elemento in lista:
        if elemento%2==0:
            listaPares.append(elemento)
        else:
            listaImpares.append(elemento)
    
    return listaPares,listaImpares

lista= [6,5,2,1,7]
pares, impares = separarParesImpares(lista)
print(pares)
print(impares)
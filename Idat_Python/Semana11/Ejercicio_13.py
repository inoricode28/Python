lista = [1,4,10,7,8,10,15]

ordernada = True
for i in range(1,len(lista)):
    if lista[i]<lista[i-1]:
        ordernada=False
        break

if ordernada:
    print("La lista esta ordenada en forma ascendente")
else:
    print("La lista NO esta ordenada en forma ascendente")






def esBisiesto(año):
    if año%400==0:
        return True
    elif año%100==0:
        return False
    elif año%4==0:
        return True
    else:
        return False

def listaBisiestos(inicio, fin):
    lista=[]
    for año in range(inicio,fin+1):
        if esBisiesto(año):
            lista.append(año)
    return lista

año1 = int(input("Año inicio: "))
año2 = int(input("Año fin: "))
lista = listaBisiestos(año1,año2)

print("Año bisiestos entre {} y {}: {}".format(año1,año2,lista))


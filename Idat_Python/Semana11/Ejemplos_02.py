#        0    1   2   3  4   5   6
lista = [20,  35, 98, 12, 72, 10, 19]
#        -7  -6  -5  -4  -3  -2  -1 

#Acceso a un elemento de la lista
print(lista[0])
print(lista[3])
print(lista[-1])
print(lista[-2])
#Modifica  un elemento de la lista
lista[0]=100
lista[-1]=200
print(lista)
#Insertar elementos en la lista
lista.insert(1,300)
print(lista)
lista.append(400)
print(lista)
#Eliminar un elemento en la lista
del lista[4]
print(lista)
del lista[-1]
print(lista)
#Cantidad de elemenentos de una lista
print(len(lista))
#Recorrer una lista
#Forma 1
suma=0
for indice in range(len(lista)):
    suma+=lista[indice]
print("Suma: " + str(suma))
suma=0
for elemento in lista:
    suma+=elemento
print("Suma: " + str(suma))
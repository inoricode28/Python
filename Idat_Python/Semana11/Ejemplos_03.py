#Slices
#        0    1   2   3  4   5   6
lista = [20,  35, 98, 12, 72, 10, 19]
#        -7  -6  -5  -4  -3  -2  -1 

lista2 = lista[:]
print(lista2)
lista3 = lista[1:-2]
print(lista3)
lista4 = lista[1:5]
print(lista4)
lista5 = lista[::2]
print(lista5)

del lista[1:-2]
print(lista)

del lista[:]
print(lista)

del lista
print(lista)

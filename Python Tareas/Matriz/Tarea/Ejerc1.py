"""
1.Se tiene una matriz de orden N x N con números al azar, invierta 
el contenido de cada una de las columnas.
"""
import random
lista = []

for z in range(5):
    lista.append([])
    # print(lista)
    for x in range(5):
        lista[z].append(random.randint(10, 20))
        #print(lista)

for j in range(5):
    print(lista[j])
    
print("\n")
lista.reverse()
# print(lista) 

for i in range(5):
    print(lista[i])
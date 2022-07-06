"""
3.En una matriz de 5 x 8 con números al azar indique que columna 
tiene le mayor promedio.
"""
import random

lista = []

for z in range(5):
    lista.append([])
    for x in range(8):
        lista[z].append(random.randint(10, 99))

for j in range(5):
    print(lista[j])

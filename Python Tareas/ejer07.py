"""
2.Escriba un programa que reciba como entrada un entero n y una 
matriz cuadrada (n x n) de enteros e imprima los elementos que 
conforman la diagonal que inicia en la esquina superior derecha y 
termina en la esquina inferior izquierda.
"""
import random
matriz = []

n = int(input("Ingrese numero de filas y columnas: "))

for z in range(n):
    matriz.append([])
    # print(matriz)
    for x in range(n):
        matriz[z].append(random.randint(10, 99))

for i in range(n):
    print(matriz[i])

for i in range(n):
    print(matriz[i][-i-1])
  

   
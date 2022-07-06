import random

matriz=[]  ###crear la matriz

cant_elem=int(input("Ingresar cantidad de filas y columnas: "))

for fila in range(cant_elem):  ##Recorrer filas con for
    matriz.append([])     ##Crear las filas
    print(matriz)
    for columnas in range(cant_elem): ##Recorrer columnas
        matriz[fila].append(random.randint(10,99))  ##ingresamos los valores
        print(matriz)

# print(matriz)

for i in range(cant_elem):  ##imprimimos la tabla
    print(matriz[i])
for i in range(cant_elem):
    print(matriz[i][i])
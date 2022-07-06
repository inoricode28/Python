"""
Crear un ejercicio de n x n, valores 
Muestre los valores de la diagonal principal
"""

m = []
n = int(input("Ingrese el total de filas y columnas de la matriz: "))

for i in range(n):
    m.append([])
    print(m) # Crea dentro de la matriz las filas sin nada
    for j in range(n):
        m[i].append(int(input("Ingrese el valor de la fila "+str(i+1)+" columna "+str(j+1)+" :")))
        print(m) # Ingresa los numeros al los sub listas dentro de la matriz
print("Los valores de la diagonal principal son: ")
print(m,"\n")

for i in range(n):  # ordena las listas o imprime listas
    print(m[i])
for i in range(n): # escoge los numeros de la lista de forma diagonal
    print(m[i][i])

"""
Crear una lista que almacene n multiplos de un numero entero
muestre los valores de la lista
"""

mult = []

m = int(input("Ingrese numero entero: "))
n = int(input("Ingrese el total de multiplos a obtener: "))

for i in range(n):
    m*=(i+1)
    mult.append(m)

print(mult)
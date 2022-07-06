"""
Realizar la carga de valores enteros por teclado, almacenarlos 
en una lista. Finalizar la carga de enteros al ingresar el cero
Mostrar finalmente el tamaño de la lista
"""
lista = []

a = int(input("Ingrese valor [0 para finalizar]: "))

while a != 0:
    lista.append(a)
    a = int(input("Ingrese valor [0 para finalizar]: "))

print("Tamaño de la lista: ")
print(lista)
print(len(lista))
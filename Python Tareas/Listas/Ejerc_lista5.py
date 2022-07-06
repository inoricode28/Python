"""
Analizar los siguientes casos y decir que datos de salida se obtiene
"""
# Caso 1

nombre = "Maria"
edad = 25
lista = [nombre, edad]
print(lista)

# Caso 2
lista1 = [10, 20, 30, 40]
lista2 = [30, 20]
lista = lista1 + lista2 + lista1
print(lista)

# Caso 3
letras = ["A", "B", "C", "D", "E", "F", "G", "H"]
del letras[100:200] # del borra elementos
print(letras)

# Caso 4
letras = ["A", "B", "C"]
print(letras)
for i in range(len(letras)):
    letras[i]="X"
    print(letras)

# Caso 5
per_autoriz = ["Alberto", "Carmen"]
nom = input("Ingrese nombre: ")
if nom in per_autoriz:
    print("Esta autorizado")
else:
    print("No esta autorizado")
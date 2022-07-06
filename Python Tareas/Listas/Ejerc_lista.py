""" Definir una lista vacia y luego solicitar la carga de 5 enteros 
por teclado y añadirlos a la lista, Imprimir lista generada"""

lista = []
for x in range(5):
    valor = int(input("Ingrese valor entero "+str(x+1)+" :"))
    lista.append(valor)

print(lista)

for z in lista: 
    print(z)

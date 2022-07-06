"""
Se tiene una lista de n elementos de tipo entero con numeros al azar 
entre 1 a 10, indique cuantas veces se repite cada numero en el vector
"""
import random

cant = int(input("Ingrese cantidad de elementos: "))
lista=[]
lista2=[]
lista_final=[]

for i in range(1, cant+1):
    num=random.randint(1, 10)
    lista.append(num)

print("Lista", lista)

for m in lista:
    n=lista.count(m)
    x = "El numero "+str(m)+" aparece "+str(n)+" ves/veces en la lista "
    lista2.append(x)

for j in lista2:
    if j not in lista_final:
        lista_final.append(j)
print("\n".join(lista_final))
print("Fin")
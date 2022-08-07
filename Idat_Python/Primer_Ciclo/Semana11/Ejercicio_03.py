from random import randint

lista=[]

for i in range(10):
    numero=randint(1,50)
    lista.append(numero)

menor = lista[0]
mayor = lista[0]

for i in range(1,len(lista)):
    if lista[i]>mayor:
        mayor=lista[i]
    if lista[i]<menor:
        menor=lista[i]

print(lista)
print("Mayor:",mayor)
print("Menor:",menor)
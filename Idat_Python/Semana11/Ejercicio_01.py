from random import randint

lista=[]

for i in range(10):
    numero = randint(1,20)
    lista.append(numero)

for i in range(len(lista)):
    print("lista[{}]:{}".format(i,lista[i]))

#for elemento in lista:
#    print(elemento)

for elemento in lista:
    if elemento%2==0:
        print(elemento)

        
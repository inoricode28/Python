lista=[]
listaInversa=[]

for i in range(5):
    cadena=input("Ingrese un texto: ")
    lista.append(cadena)

for elemento in lista:
    listaInversa.insert(0,elemento)

print(lista)
print(listaInversa)

listaInversaSlice = lista[::-1]
print(listaInversaSlice)

#lista = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
#listaInversa = ['cinco','cuatro','tres','dos','uno']
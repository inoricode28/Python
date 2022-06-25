lista =  [10, 18, 12, 15, 8, 9, 20, 13, 11, 5]

#a. Copiar todos los elementos de la lista a una nueva lista.
lista2 = lista[:] #Saca una copia de la lista
#lista2 = lista #lista2 y lista son la misma lista
#lista[0]=100
#lista[-1]=500
print(lista2)

#b. Copiar todos los elementos de la lista con índice 
# impar a una nueva lista.
lista2 = lista[1::2]
print(lista2)

#c. Obtener el último elemento de la lista

#d. Obtener los elementos de la lista menos el último.
print(lista[:-1])


#e. Obtener una nueva lista con los elementos de la lista original menos el
#primero y último.
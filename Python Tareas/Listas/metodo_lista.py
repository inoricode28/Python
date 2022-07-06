""" .append()
Este metodo nos permite agregar nuevos elementos 
a una lista"""
lista = [2.5, "DevCode", 1.2, 5]
print(lista)
lista.append([10]) # lista.append(10)
print(lista)

""" .extend()
Extend tambien nos permite agregar elementos dentro de una lista, pero a 
diferente de append al momento de agregar una lista, cada elemento de esta
lista se agrega como un elemento mas dentro de la otra lista"""

lista.extend([2.5])
print(lista)

""" .remove()
El motodo remove va a remover un elemento que se le pase como parametro dentro de
la lista donde se le esta aplicando"""

lista.remove(2.5)
print(lista)
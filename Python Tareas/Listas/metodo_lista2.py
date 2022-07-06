""" .index()
Index devuelve el numero de indice del elemento que le 
pasemos por parametro"""
lista = [2.5, "DevCode", 1.2, 5, 5]
print(lista.index("DevCode"))

""" .count()
Para saber cuantas veces un elemento de una lista se repite podemos 
utilizar el metodo count()."""
print(lista.count(5))

""" .reverse()
Tambien podemos invertir los elementos de una lista"""
lista.reverse() # el reverse no se puede poner dentro del print, bota error 
print(lista)
from Motor import factorial
from Motor import separarParesImpares
from Motor import listaBisiestos
numero=int(input('Ingrese un numero: '))
print("El factorial de",numero,"es: ",factorial(numero))

print()

lista= [6,5,2,1,7]
pares, impares = separarParesImpares(lista)
print(pares)
print(impares)

print()

año1 = int(input("Año inicio: "))
año2 = int(input("Año fin: "))
lista = listaBisiestos(año1,año2)

print("Año bisiestos entre {} y {}: {}".format(año1,año2,lista))

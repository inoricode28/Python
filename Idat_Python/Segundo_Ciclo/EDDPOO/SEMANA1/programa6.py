from area_cuadrado import cuadrado
from area_rectangulo import rectangulo
from area_trapecio import trapecio

lado=int(input('Ingrese el lado del cuadrado: '))
print("El area del cuadrado es: ", cuadrado(lado))

base=int(input('Ingrese la base del rectangulo:'))
altura=int(input('Ingrese la altura de l rectangulo: '))
print("El area es: ", rectangulo(base, altura))
BMR=int(input('Ingrese el Base Mayor del trapecio: '))
BMNR=int(input('Ingrese el Base Menor del trapecio: '))
Altura=int(input('Ingrese la altura: '))
print("EL area es: ",trapecio(BMR,BMNR,altura))

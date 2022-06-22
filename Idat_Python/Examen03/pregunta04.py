#Ingrese de datos
from random import randint

#Proceso
ContMayor_1000=0
Cont_menor_1000=0


while True:
    n = randint(500,1500)
    if n>1000:
        ContMayor_1000+=1
    else:
        Cont_menor_1000+=1

    print(n, end=" ")

    if n >1000 and n%2!=0 and n<1050:
        break 
#Salida de datos


print("\nCantidad de números mayores de 1000: " + str(ContMayor_1000))
print("Cantidad de números menores o igual 1000: " + str(Cont_menor_1000))
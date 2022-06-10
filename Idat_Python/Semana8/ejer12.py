from random import randint

SumaSueldo=0
suma=0
contador=0
contMayor=0
contMenorIgual=0

while True:
    sueldo = randint(2500,3500)
    contador+=1
    SumaSueldo+=sueldo
    print("Sueldo N {}: {}".format(contador, sueldo))

    if sueldo>3000:
        contMayor+=1
    else:
        contMenorIgual+=1

    if sueldo==2500 or sueldo==3500:
        break
promedio = round(SumaSueldo/contador,2)

print("Sueldo promedio: "+str(promedio))
print("Cantidad de sueldo mayores a 3000: "+str(contMayor))
print("Cantidad de sueldo menores o iguales a 3000: "+str(contMenorIgual))
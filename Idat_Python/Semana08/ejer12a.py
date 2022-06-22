from random import randint

n=int(input('Ingrese numero de sueldos: '))
inicio=1
SM_3000=0
suma=0
while inicio<=n:
    numero= randint(2500,3500)
    if numero>3000:
        SM_3000+=1
    suma+=numero
    print(numero)
    inicio+=1
promedio =suma/n
print("El sueldo promedio es: "+str(promedio))
print("La cantidad Mayores que 3000: "+str(SM_3000))
print("La cantidad Menores o iguales que 3000: ",n-SM_3000)


    





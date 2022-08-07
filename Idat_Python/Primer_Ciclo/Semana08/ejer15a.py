from random import randint
n=int(input('Ingrese numero de edades: '))
inicio=1
suma=0
mayores=0
while inicio<=n:
    edad= randint(14,70)
    if edad>=18:
        mayores+=1
    suma+=edad
    print(edad,"Años")
    inicio+=1
promedio =suma/n
print("La edad promedio es: "+str(promedio))
print("Los mayores de edad son: : "+str(mayores))
print("Los menores de edad son: : "+str(n-mayores))
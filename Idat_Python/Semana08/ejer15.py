from random import randint
n=int(input('Ingrese numero de edades: '))
inicio=1
suma=0
mayores=0
more=0
while inicio<=n:
    edad= randint(14,70)
    if edad>45 and edad<50:
        more+=edad
    if edad>=18:
        mayores+=1
    suma+=edad
    print(edad,"Años")
    inicio+=1
promedio =suma/n
promedio1= more/n
print("La edad promedio entre 46 y 49 es: "+str(promedio1))
print("La edad promedio es: "+str(promedio))
print("Los mayores de edad son: : "+str(mayores))
print("Los menores de edad son: : "+str(n-mayores))
from random import randint
sumyear=0
contedad=0
contMayor=0
contMenor=0

while True:
    edad = randint(14,70)
    contedad+=1
    sumyear+=edad
    
    print("Persona N°",contedad, "tiene",edad, "años de edad: ")
    
    if edad >=18:
        contMayor+=1
    else:
        contMenor+=1

    if edad > 45 and edad < 50 :
        break
promedio = round(sumyear/contedad,2)

print("\nEl promedio de edades es: " + str(promedio))
print("La cantidad de mayores de edad: " + str(contMayor))
print("La cantidad de menores de edad: " + str(contMenor))
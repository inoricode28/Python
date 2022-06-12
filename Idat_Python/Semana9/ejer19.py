from random import randint
year=0
menores=0
mayores=0
for i in range(1,46):
    edad= randint(18,70)
    print(edad,end=" ")
    year+=edad
    promedio = year/45
    if edad<=30:
        menores+=1
    elif edad>30:
        mayores+=1

print("\nEL promedio es: ",round(promedio,2))
print("Menores o iguales a 30 es: ",str(menores))
print("Mayores de 30 es: ",str(mayores))

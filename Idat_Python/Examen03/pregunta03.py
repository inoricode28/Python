from random import randint

STN=0
contN=0
contAP=0
contDPS=0

while True:
    nota = randint(0,100)
    contN+=1
    STN+=nota
    print("La nota del alumno N°",contN,"es: ",nota)

    if nota >=70:
        contAP+=1
    else:
        contDPS+=1

    if contN ==40:
        break
promedio = round(STN/contN,2)

print("\nLa nota promedio es:: " + str(promedio))
print("Alumnos aprobados: " + str(contAP))
print("Alumnos desaprobados: " + str(contDPS))
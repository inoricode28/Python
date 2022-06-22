#Ingreso de datos

nota = int(input("Ingrese su calificación: "))

#Proceso

if nota < 0 or nota >20:
    nota = -1

if nota <11 or nota>=0:
    nota = nota

if nota >=12 and nota <19:
    nota +=2

if nota ==19 or nota ==20:
    nota = 20

if nota ==-1:
    print("Nota no valida")

#Salida de datos

print ("Su calificación es de: " + str (nota))
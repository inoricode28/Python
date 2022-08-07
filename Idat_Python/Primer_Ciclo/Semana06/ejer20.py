#Ingreso de datos
tardanza = float(input("Ingrese su tiempo de tardanza: "))
observaciones = int(input("Ingrese la cantidad de observaciones: "))
#Proceso
if tardanza ==0:
    puntajeT = 10
elif tardanza <=2:
    puntajeT = 8
elif tardanza <=5:
    puntajeT = 6
elif tardanza <=9:
    puntajeT = 4
else:
    puntajeT = 2
if observaciones ==0:
    puntajeO = 10
elif observaciones ==1:
    puntajeO = 8
elif observaciones ==2:
    puntajeO = 5
elif observaciones ==3:
    puntajeO = 1
else:
    puntajeO = 0

puntajeTotal = puntajeT + puntajeO

if puntajeTotal <11:
    bono = puntajeTotal * 2.5
elif puntajeTotal <=13:
    bono = puntajeTotal * 5
elif puntajeTotal <=16:
    bono = puntajeTotal * 7.5
elif puntajeTotal <=19:
    bono = puntajeTotal * 10
else:
    bono = puntajeTotal * 12.5
#Salida de datos

print ("El puntaje por puntualidad es: " + str(puntajeT))
print ("El puntaje por rendimiento es: " + str(puntajeO))
print ("El puntaje total es: " + str(puntajeTotal))
print ("Su bonificación es de: " + str(bono)) 
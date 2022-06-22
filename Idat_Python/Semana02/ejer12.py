#Ingreso de datos

r = 25
h = 50
π = 3.1416

#Proceso

areaBase = π * r**2
areaLateral = 2 * π * r * h
areaTotal = ((2*areaBase) + areaLateral)

#Salida de datos

print ("Para calcular el área de este cilindro debemos saber que contamos con un área base de: {} ,área lateral de: {} , por lo que su área total seria de: {}.".format(areaBase,areaLateral,areaTotal))
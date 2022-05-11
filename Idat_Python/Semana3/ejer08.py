#Entrada de datos
numero = int(input("Ingresar un número de 4 cifras: "))

#Proceso
millar = numero // 1000 %10
unidad = numero % 10

numeroNuevo = millar*10 + unidad

#Salida de datos
print ("La suma de cifras millar y unidad es: " + str(numeroNuevo))
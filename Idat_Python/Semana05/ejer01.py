#Ingresante
velocidad=float(input('Ingrese la velocidad: '))

#Proceso

if velocidad <0:
    mensaje = "velocidad no valida"
if velocidad >70 and velocidad<=90:
    mensaje = "La multa es S/100.00"
if velocidad>90 and velocidad<=100:
    mensaje = "La multa es S/140.00"
if velocidad>100:
    mensaje = "La multa es S/200.00"

#Mostrar lo resultados

print ("La multa es: " + str(mensaje))
#Ingreso de datos
dia = int(input("Día de pago: "))
cuota = float(input("Cuota mensual en dólares: "))
#Proceso
if dia<=10:
    if cuota*2/100 > 5:
        adicional = -cuota*2/100
    else:
        adicional = -5
elif dia<=20:
    adicional = 0
else:
    if cuota*3/100 > 10:
        adicional = cuota*3/100
    else:
        adicional = 10
montoPagar = cuota + adicional
#Mostrar datos
print("Monto a pagar: " + str(montoPagar))
#Ingresante
horas_trabajadas=float(input("Horas a trabajar: "))
tarifa_hora=float(input("tarifa por hora: "))
#Calculo
sueldo_bruto=horas_trabajadas*tarifa_hora
descuento_Essalud=sueldo_bruto*(11.5/100)
descuento_ONP=sueldo_bruto*(12.5/100)

decuento_total=descuento_Essalud+descuento_ONP

sueldo_neto= sueldo_bruto-decuento_total
print("El sueldo bruto es: ",sueldo_bruto)
print("Descuento de EsSalud: {:.2f}".format(descuento_Essalud))
print("Descuento de ONP: ",descuento_ONP)
print("Total Descuento: {:.2f}".format(decuento_total))
print("El sueldo neto es: ",sueldo_neto)

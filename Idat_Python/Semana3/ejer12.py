#Entrada de datos
donacion = int(input("Ingrese el monto de donación: "))

#Proceso
medicinaGeneral = 45/100 * donacion
ginecologia = 30/100 * donacion
pediatria = 20/100 * (medicinaGeneral + ginecologia)
traumatologia = donacion - (medicinaGeneral + ginecologia + pediatria)

#Salida de datos
print ("La donación se repartira de la siguiente forma: \nMedicina General recibira: " + str(medicinaGeneral))
print ("Ginecologia recibira: " + str(ginecologia))
print ("Pediatria recibira: " + str(pediatria))
print ("Traumatologia recibira: " + str(traumatologia))
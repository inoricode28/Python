#Ingreso de datos
tardanza=float(input("Ingrese las horas de ausencia:"))
tornillosdef=int(input("Ingrese la cantidad de tornillos defectuosos: "))
tornillosNOdef=int(input("Ingrese la cantidad de tornillos no defectuosos producidos: "))

#Proceso

if tardanza >90 and tornillosdef >=300 and tornillosNOdef <= 10000:
    efiC = "Grado 5"
elif tardanza <=90 and tornillosdef >=300 and tornillosNOdef <= 10000:
    efiC = "Grado 7"
elif tardanza >90 and tornillosdef <300 and tornillosNOdef <= 10000:
    efiC = "Grado 8"
elif tardanza >90 and tornillosdef >=300 and tornillosNOdef >10000:
    efiC = "Grado 9"
elif tardanza <=90 and tornillosdef <300 and tornillosNOdef <= 10000:
    efiC = "Grado 12"
elif tardanza <=90 and tornillosdef >=300 and tornillosNOdef >10000:
    efiC = "Grado 13"
elif tardanza >90 and tornillosdef <300 and tornillosNOdef >10000:
    efiC = "Grado 15"
else:
    efiC = "Grado 20"

print("Su condición es: " +str(efiC))
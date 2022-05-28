#Ingreso de datos
Medidas = int(input("Ingrese la magnitud del ángulo: "))
if Medidas >=0 and Medidas <=360:
    #Proceso
    if Medidas ==0:
        Calsificacion = "Nulo"
    elif Medidas >0 and Medidas <90:
        Calsificacion = "Agudo"
    elif Medidas ==90:
        Calsificacion = "Recto"
    elif Medidas >90 and Medidas <180:
        Calsificacion = "Obtuso"
    elif Medidas ==180:
        Calsificacion = "Llano"
    elif Medidas >180 and Medidas <360:
        Calsificacion = "Cóncavo"
    else:
        Calsificacion = "Completo"
    print("La clasificación del ángulo ingresado es: " + str(Calsificacion))  

  #Salida de datos 
else:
    print ("LA MAGNITUD DEL ÁNGULO INGRESADO NO ES VALIDA")




    
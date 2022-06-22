
#ingreso de datos
numero=int(input('Ingrese numero de intervalo[1-4]: '))
#Proceso
if not(numero>=1 and numero<=4):
    mensaje = "Estado ingresada es incorrecto"
    print(mensaje)
else:
    if numero==1:
        estado = "Soltero"
    elif numero==2:
        estado = "Casado"
    elif numero ==3:
        estado = "Viudo"
    elif numero==4:
        estado = "Divorciado"
    
    print("El estado es: " +str(estado))

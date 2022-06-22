#ingreso de datos
numero=int(input('Ingrese numero: '))
#Proceso
if not(numero>=1 and numero<=7):
    mensaje = "Dia ingresada es incorrecto"
    print(mensaje)
else:
    if numero==1:
        dia = "Lunes"
    elif numero==2:
        dia = "Martes"
    elif numero ==3:
        dia = "Miercoles"
    elif numero==4:
        dia = "Jueves"
    elif numero ==5:
        dia = "Viernes"
    elif numero==6:
        dia = "Sabado"
    elif numero ==7:
        dia = "Domingo"
    print("El dia es: " +str(dia))
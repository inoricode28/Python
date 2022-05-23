#ingreso de datos
numero=int(input('Ingrese numero: '))
#Proceso
if numero%7==0:
    dia = "Lunes"
elif numero%7==1:
    dia = "Martes"
elif numero%7==2:
    dia = "Miercoles"
elif numero%7==3:
    dia = "Jueves"
elif numero%7==4:
    dia = "Viernes"
elif numero%7==5:
    dia = "Sabado"
elif numero%7==6:
    dia = "Domingo"
print("El dia es: " +str(dia))
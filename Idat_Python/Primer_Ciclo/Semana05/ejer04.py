dia=int(input('Ingrese un dia del [1-7]: '))
if dia<=0 or dia>=8:#Try
    dia =-1
if dia== 1:
    mensaje= "Lunes"

if dia== 2:
    mensaje= "Martes"

if dia== 3:
    mensaje= "Miercoles"

if dia== 4:
    mensaje= "Jueves"

if dia== 5:
    mensaje= "Viernes"

if dia== 6:
    mensaje= "Sabado"

if dia== 7:
    mensaje= "Domingo"

if dia==-1:#Catch
    print("Dia no es valida")

if dia!=-1:
    print("El dia de la semana es: "+str(mensaje))
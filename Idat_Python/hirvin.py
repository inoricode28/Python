notas=int(input("ingrese notas: "))

if notas<=0 and notas>=21:
    notas =-1 #try
if notas>=11 and notas<19:
    notas=notas+2
if notas<20:
    notas = 20

if notas==-1:#catch
    print("Nota no es valida")

if notas !=-1:#diferente de
    print("Nota final es: ",notas)
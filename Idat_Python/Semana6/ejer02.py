nota=int(input('Ingrese nota: '))
if not(nota>=0 and nota<=20):
    mensaje= "nota ingresada es incorrecto"
    print(mensaje)
else:
    if nota>=17:
        mensaje = "A"
    elif nota>=14 and nota<17:
        mensaje="B"
    elif nota>=12 and nota<14:
        mensaje="C"
    elif nota<12:
        mensaje="D"
    print("La categoria es: "+str(mensaje))

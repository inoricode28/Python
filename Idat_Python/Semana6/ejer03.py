velocidad=int(input('Ingrese velocidad: '))

if velocidad>=71:
        multa = "S/. 100"
elif velocidad>=91:
    multa = "S/. 140"
else:
    multa = "S/. 200"

#salida de datos
print("Su multa sera de:" +str(multa))

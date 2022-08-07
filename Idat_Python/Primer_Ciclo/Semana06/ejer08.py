temperatura=int(input('Ingrese temperatura: '))
if not(temperatura>=-98 and temperatura<=56):
    mensaje= "No se ha registrado una temperatura de ese valor"
    print(mensaje)
else:
    if temperatura<=10:
        mensaje = "Frio"
    elif temperatura>10 and temperatura<=20:
        mensaje="Nublado"
    elif temperatura>20 and temperatura<=30:
        mensaje="Caluroso"
    elif temperatura>30:
        mensaje="Tropico"
    print("La temperatura es: "+str(mensaje))
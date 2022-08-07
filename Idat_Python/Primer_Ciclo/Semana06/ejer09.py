fierro=float(input('Ingrese valores de fierro: '))
if not(fierro>=0 and fierro<=100):
    mensaje= "No es un porcentaje valido"
    print(mensaje)
else:
    if fierro<0.05:
        mensaje="Bessemer"
    elif fierro>=0.05 and fierro<=0.18:
        mensaje="No Bessemer"
    elif fierro>0.18:
        mensaje="Fosforo"
    print("La clasificacion es: "+str(mensaje))
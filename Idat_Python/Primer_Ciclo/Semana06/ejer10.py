tallo=float(input('Ingrese la altura del tallo: '))
if not(tallo>0 and tallo<=115):
    mensaje= "No es una altura valido"
    print(mensaje)
else:
    if tallo<=1:
        mensaje="Mala"
    elif tallo>1 and tallo<=4:
        mensaje="Arbusto"
    elif tallo>4 and tallo<=8:
        mensaje="Arbolito"
    elif tallo>8:
        mensaje="Arbol"
    print("La clasificacion es: "+str(mensaje))
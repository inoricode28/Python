dia=int(input('Ingrese los dias: '))

if not(dia>0):
    mensaje= "Dias no es valido"
    print(mensaje)
else:
    obsequio = "Ganaste un cuaderno"
    if dia==1:
        alquiler=50*dia        
    elif dia == 2:
        alquiler=45*dia
    elif dia>=3 and dia<=5:
        alquiler=40*dia
    elif dia>=6 and dia<=10:
        alquiler=35*dia
    elif dia>10:
        alquiler=30*dia
        obsequio = "Ganaste una agenda"
    print("El alquiler es: "+str(alquiler))
    print(obsequio)

    
         
    
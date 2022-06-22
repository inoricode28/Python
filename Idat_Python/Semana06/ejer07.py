#Entrada de datos
peso=float(input("Peso: "))
altura=float(input("Altura: "))

#Proceso
IMC=peso/altura**2

if IMC<20:
    grado="Delgado"
elif IMC>=20 and IMC<25:
     grado="Normal"
elif IMC>=25 and IMC<30:
     grado="Sobrepeso"
elif IMC>=30:
     grado="Obesidad"

#Salida de datos
print("Su peso es: ", grado)
#Igreso de datos
numero=int(input("Ingrese un numero entero: "))

#Proceso
if numero>0:
  signo = "Positivo"
if numero<0:
    signo= "Negativo"
if numero==0:
    signo = "Cero"

print("Signo: " + signo)
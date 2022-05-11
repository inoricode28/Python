num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))

#Proceso
mayor=num1
if num2>mayor:
    mayor=num2
if num3>mayor:
    mayor=num3

#Salida

print("Mayor: "+str(mayor))
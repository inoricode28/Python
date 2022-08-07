n1=int(input("Ingrese el primer numero: "))
n2=int(input("Ingrese el segundo numero: "))
n3=int(input("Ingrese el tercer numero: "))

if n1>n2>n3:
    resultado= "Numero1 es el mayor"
if n2>n3>n1:
    resultado= "Numero2 es el mayor"
if n3>n2>n1:
    resultado= "Numero3 es el mayor"

#Salida

print(resultado)
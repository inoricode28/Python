"""Cada alumno deberá realizar un programa que tenga 4 funciones que permita sumar,
restar, multiplicar y dividir, a su vez deberá pedir dos números enteros, además
de ingresar la operación que desea realizar, usando condicionales deberá aplicar una de
las operaciones, el programa debe tener manejo de excepciones."""

def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print("No se puede dividir entre 0...!!!!")
        return "Operacion erronea...!!!"

while True:
    try:
        num1=int(input('Ingrese el primer numero: '))
        num2=int(input('Ingrese el segundo numero: '))
        break
    except ValueError:
        print("Los valores ingresados son incorrectos, ingrese nuevamente los numeros...!!!!")

operacion = input('Ingrese la operacion a realizar: \n- Suma\n- Resta \n- Multiplicacion\n- Division\n\n> ').upper()

if operacion =="SUMA":
    print("SUMA: ",suma(num1,num2))
elif operacion =="RESTA":
    print("RESTA: ",resta(num1,num2))
elif operacion =="MULTIPLICACION":
    print("MULTIPLICACION: ", multiplicacion(num1,num2))
elif operacion =="DIVISION":
    print("DIVICION: ",division(num1,num2))
else:
    print("Operacion no contemplada")

print("Gracias por usar el programa...!!!")


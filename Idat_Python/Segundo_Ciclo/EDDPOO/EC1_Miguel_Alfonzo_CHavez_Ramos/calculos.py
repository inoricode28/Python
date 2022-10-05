from operaciones import potenciacion
from operaciones import resta
from operaciones import suma
from operaciones import cociente
from operaciones import producto

while True :
    try:
        num1 = int(input("Ingrese el primer numero:"))
        num2 = int(input("Ingrese el segundo numero:"))
        break
    except ValueError:
        print("Tipo de dato no valido")
        
operacion= input("Ingrese la operacion a realizar:\n- SUMA\n-RESTA\n- MULTIPLICACION\n-DIVISION\n-POTENCIACION\n\n> ").upper()


if operacion =="SUMA":
    print("la suma es : ", suma(num1,num2))
elif operacion =="RESTA":
    print("la diferencia es:", resta(num1, num2))
elif operacion =="MULTIPLICACION":
    print("El producto es :", producto(num1,num2))
elif operacion =="DIVISION":
    print("El cociente es : " , cociente(num1,num2))
elif operacion =="POTENCIACION":
    print("La potenciacion es :", potenciacion(num1,num2))
else:
    print("Operacion no completada")
#Ingreso de datos

numero = int(input("Ingrese un número de 5 cifras: "))

#Proceso

if numero >= 10000 and numero <= 99999:
    quintoDigito = numero // 10000
    cuartoDigito = numero // 1000 % 10
    tercerDigito = numero // 100 % 10
    segundoDigito = numero // 10 % 10
    primerDigito = numero % 10
    if (quintoDigito and cuartoDigito == segundoDigito and primerDigito):
        mensaje = "El número es capicua"
    else:
            mensaje = "El número no es capicua"
else:
    mensaje = "Ingrese un número de 5 digitos CAPICUA"

#Salida de datos

print(mensaje)
#Ingreso de datos
numero=int(input('Ingrese un # de 3 cifras: '))

if numero>=100 and numero<=999:
    c = numero//100
    d = numero//10%10
    u = numero%10
    #123
    #543
    if (c==d-1 and d==u-1)or(c==d+1 and d==u+1):
        mensaje = "Cifras consecutivas"
    else:
        mensaje = "Cifras NO consecutivas"
else:
    mensaje = "El numero debe ser positivo de 3 cifras"

#Mostrar resultados
print(mensaje)

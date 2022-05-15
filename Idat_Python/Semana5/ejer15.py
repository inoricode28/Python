numero=int(input('Digite un numero entero positivo: '))

if numero>=0:
    if str(numero)==str(numero)[::-1]:
        print('%i es capicua. '%numero)
    else:
        print('%i no es capicua. '%numero)
else:
    print('El numero debe ser positivo.')

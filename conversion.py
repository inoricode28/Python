menu = """ 
Bienvenido al conversor de monedas 🤑

1 - Pesos colombianos
2 - Pesos argentinos
3 - Soles peruanos
4 - Pesos mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("¿Cuantos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")   
elif opcion == 2:
    pesos = input("¿Cuantos pesos mexicanos tiene?: ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 3:
    soles = input("¿Cuantos soles peruanos tienes?: ")
    soles = float(soles)
    valor_dolar = 3.90
    dolares = soles / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares) 
    print("Tienes $" + dolares + "dolares")
elif opcion == 4:
    pesos = input("¿Cuntos pesos mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dolares") 

else:
    print('Ingresa una opcion correcta por favor')

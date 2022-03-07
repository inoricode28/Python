def conversor(tipos_pesos, Valor_dolar):
    pesos = input("¿Cuantos pesos " + tipos_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / Valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")   

def conversor01(tipos_pesos, Valor_dolar):
    pesos = input("¿Cuantos soles " + tipos_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / Valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")


menu = """ 
Bienvenido al conversor de monedas 🤑

1 - Pesos colombianos
2 - Pesos argentinos
3 - Soles peruanos
4 - Pesos mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor01("peruanos",3.90 )
elif opcion == 4:
    conversor("mexicanos", 24)

else:
    print('Ingresa una opcion correcta por favor')
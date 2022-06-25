lista=[]

while True:
    numero = int(input("Ingrese un número: "))
    if numero>=0:
        lista.append(numero)
    else:
        break

print(lista)

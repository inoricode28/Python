suma=0
cont=0
lista=[]
while True:
    numero = int(input("Ingrese un número: "))
    if numero!=0:
        cont+=1
        suma+=numero
        promedio=suma/cont
        lista.append(numero)
    else:
        break
print(lista)
print(suma)
print(promedio)
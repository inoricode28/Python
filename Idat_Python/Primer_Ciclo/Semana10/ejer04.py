from random import randint
print("Número\tCantidad de divisores")
while True:
    numero=randint(1,1000)
    cantidad=0

    for i in range(1,numero+1):
        if numero%i==0:
            cantidad+=1

    print(str(numero) + "\t" + str(cantidad))

    if cantidad==4:
        break
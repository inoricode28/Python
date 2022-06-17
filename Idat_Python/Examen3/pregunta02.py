from random import randint

cont=0
NMY=9
NMN=100

while True:
    n=randint(10,99)
    cont+=1
    print("El número N°",cont, "es: ",n)
    

    if n>NMY:
        NMY=n
    elif n<NMN:
        NMN=n

    decena = n // 10%10
    unidad = n % 10 

    if decena + unidad== 3 or decena + unidad ==5:
        break

print("\nLa cantidad de números generados es: " + str(cont))
print("Mayores números: " + str(NMY))
print("Menores números: " + str(NMN))

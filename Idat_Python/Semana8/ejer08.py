from random import randint
suma=0
conPares=0
contImpares=0
sumaPares=0
sumaImpar=0
while True:
    numero= randint(100,999)
    if numero%2==0:
        conPares+=1
        sumaPares+=numero
    else:
        contImpares+=1
        sumaImpar+=numero
    suma+=numero
    print(numero,end=" ")
    
    if numero%2==0 and numero>=500:
        break
print("\nSuma: "+str(suma))
print("Cantidad de pares: "+str(conPares))
print("Cantidad de impares: "+str(contImpares))
print("Suma de pares: "+str(sumaPares))
print("Suma de impares: "+str(sumaImpar))
from random import randint
i=1
contador=0
while i<=200:
    numero=randint(100,999)
    centena=numero//100
    unidad = numero%10
    if centena==unidad:
        print(numero, end=" ")
        contador+=1
    i+=1        

print("\nCantidad de capicuas "+str(contador))
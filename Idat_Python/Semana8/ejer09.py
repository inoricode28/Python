from random import randint

rango1=0
rango2=0
rango3=0
rango4=0

while True:
    numero=randint(200,600)
    if numero<=300:
        rango1+=1
    elif numero<=400:
        rango2+=1
    elif numero<=500:
        rango3+=1
    else:
        rango4+=1
    print(numero, end=" ")

    if numero%2!=0 and numero>400 and numero<500:
        break

print("Cantidad>=300: " + str(rango1))
print("Cantidad > 300 y <= 400: " + str(rango2))
print("Cantidad > 400 y <= 500: " + str(rango3))
print("Cantidad > 500 y <= 600: " + str(rango4))
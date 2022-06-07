#Diseñe un programa que imprima y sume
#la siguiente serie: 1, 2, 3, ..., 100

i=1
suma=0
while i<=100:
    print(i, end=" ")
    suma+=i
    i+=1
print("\nSuma: "+str(suma))
    

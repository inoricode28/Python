#Diseñe un programa que imprima y sume
#la siguiente serie: 3, 10, 17, ..., 94
i=3
suma=0
contador=0
while i<=94:
    print(i,end=" ")
    suma+=i #Acumulador
    i+=7
    contador+=1 #Contador
print("\suma: "+str(suma))
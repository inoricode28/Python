#Diseñe un programa que imprima y sume la siguiente serie:
# 100, 99, 98, …, 1
suma=0
for i in range(100,0,-1):
    print(i,end=" ")
    suma+=i

print("\nSuma: "+str(suma))


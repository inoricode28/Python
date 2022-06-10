#Diseñe un programa que imprima y sume la siguiente serie:
# 0,1,2,3, … ,50
suma=0
for i in range(51):
    print(i,end=" ")
    suma+=i
print("\nSuma: "+str(suma))
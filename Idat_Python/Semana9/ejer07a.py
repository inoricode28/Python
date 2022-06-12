#Diseñe un programa que imprima y sume 12 términos de la siguiente serie:
#6, 8, 12, 20, 36, ...
2-4-8-16

while True:
    n=int(input("Ingrese un numero: "))
    t,suma=5,0
    for i in range(0,n):
        t+=2**i
        print(t,end=" ")
        suma+=t
    print("\nTermino",n,"=",t)
    print("La suma hasta el termino",n,"es: ",suma)
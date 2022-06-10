#Diseñe un programa que imprima y sume 25 términos de la siguiente serie:
#2, 7, 4, 9, 8, 11, 16, 13 ...
#

while True:
    n=int(input())
    t,suma=5,0
    for i in range(0,n):
        t+=2**i
        suma+=t
    print("Termino",n,"=",t)
    print("La suma hasta el termino",n,"es=",suma)
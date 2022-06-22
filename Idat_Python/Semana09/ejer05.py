#Diseñe un programa que imprima y sume 10 términos de la siguiente serie:
#9, 16, 25, 36, 49, 64, ...
#7-9-11-13-15-17-19-21-23-25

termino=3
suma=3
for i in range(10):
    cuadrado = termino**2
    print(cuadrado,end=" ")
    termino+=1
    suma+=cuadrado

print("\nSuma: "+ str(suma))
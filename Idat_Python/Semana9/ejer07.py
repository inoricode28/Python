#Diseñe un programa que imprima y sume 12 términos de la siguiente serie:
#6, 8, 12, 20, 36, ...
2-4-8-16

termino=6
razon=2
suma=0
for i in range(12):
    print(termino,end=" ")
    suma+=termino
    termino+=razon
    razon*=2

print("\nSuma: "+ str(suma))
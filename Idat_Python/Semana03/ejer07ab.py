#Ingreso de datos
numero=float(input("Numero de 5 cifras: "))
#proceso
#45781
#abcde
a = numero//10000
b = numero//1000%10
c = numero//100%10
d = numero//10%10
e = numero%10

#Saliente
print(str(a),str(b),str(d),str(e))
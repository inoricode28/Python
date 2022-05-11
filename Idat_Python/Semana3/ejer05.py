#Entrada de datos
numero = int(input("Ingresar un número de 5 cifras: "))

#Proceso
#12345
Millar_milla=numero //10000%1000 #1
millar=numero//1000%10 #2
centena = numero // 100%10 #3
decena = numero // 10 % 10 #4
unidad = numero % 10 #5

print(str(Millar_milla)+str(millar)+str(decena)+str(unidad))
print(Millar_milla)
print(millar)
print(centena)
print(decena)
print(unidad)
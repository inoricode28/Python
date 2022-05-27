#Ingreso de datos
cuadernos = int(input("Ingrese la cantida de cuadernos a comprar: "))

#Proceso
if cuadernos <12:
    lapiceroLucas = 0
    lapiceroCross = 0
    lapiceroNovo = 0
elif cuadernos <24:
    lapiceroLucas = cuadernos // 4
    lapiceroCross = 0
    lapiceroNovo = 0
elif cuadernos <36:
    lapiceroLucas = 0
    lapiceroCross = (cuadernos // 4) * 2
    lapiceroNovo = 0
else:
    lapiceroLucas = 1
    lapiceroCross = 1
    lapiceroNovo = (cuadernos //4)*2 

#Salida de datos

print("Lapiceros Lucas: " + str(lapiceroLucas))
print("Lapiceros Cross: " + str(lapiceroCross))
print("Lapiceros Novo: " + str(lapiceroNovo))


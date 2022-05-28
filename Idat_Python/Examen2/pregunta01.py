#Ingreso
n1=float(input("Ingrese la primera nota: "))
n2=float(input("Ingrese la segundo nota: "))
n3=float(input("Ingrese la tercer nota: "))
EP=float(input("Ingrese Examen Parcial: "))
EF=float(input("Ingrese Examen Final: "))
#Proceso
if n1<n2 and n1<n3:
    menor = n1
    PP=(n2+n3)/2
elif n2<n1 and n2<n3:
    menor = n2
    PP=(n1+n3)/2
else: 
    menor=n3
    PP=(n1+n2)/2

PP=PP*20/100
Parcial = EP*30/100
Final = EF*50/100
Promedio_final = PP+Parcial+Final
#Resultado
print("La nota eliminada es: "+str(menor))
print("El promedio es: "+str(round(Promedio_final)))


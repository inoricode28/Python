#Ingresando datos
h = float(input("Horas a Trabajar: "))
categoria = input("Tarifa por hora[A-B-C-D] ")

#Proceso de datos
if categoria=="A" or categoria=="B" or categoria=="c" or categoria=="D":
    if categoria=="A":
        suelb=h*21.0
    elif categoria=="B":
        suelb=h*19.5
    elif categoria=="C":
        suelb=h*17.0
    else:
        suelb=h*15.5
    
    if suelb>2500:
        descuento = suelb*0.2
    else:
        descuento = suelb*0.15
sueldon = suelb-descuento

# saliente
print("El Sueldo bruto es: S/. "+str(suelb))
print("El descuento es: S/. "+str(descuento))
print("El Sueldo neto es: S/. "+str(sueldon))
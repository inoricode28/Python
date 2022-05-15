#Ingreso de datos
donacion = float(input("Donacion: "))

#Proceso
if donacion>=10000:
    centroSalud = donacion*30/100
    comedor = donacion*50/100
    bolsa = donacion-(centroSalud+comedor)
else:
    centroSalud=donacion*25/100
    comedor=donacion*60/100
    bolsa = donacion-(centroSalud+comedor)

print("Centro de salud: " + str(centroSalud))
print("Comedor: " + str(comedor))
print("Bolsa: " + str(bolsa))
    
